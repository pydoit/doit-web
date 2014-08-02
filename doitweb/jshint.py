import json
import copy

from pathlib import Path
from mergedict import ConfigDict
from doit.tools import config_changed
from doitcmd import BaseCommand



class JsHint(BaseCommand):
    cmd_template = 'jshint {opts} {js_file}'

    def __init__(self, config=None, **opts):
        """
        @param config: (str) config path
        """
        super(JsHint, self).__init__(options=opts)
        if config:
            with open(config, 'r') as fp:
                self._config = ConfigDict(json.load(fp))
        else:
            self._config = {}


    def __call__(self, config_file, js_file):
        """return task metada to jshint single file"""
        opts = self.opt_str(self.options, {'config': config_file})
        cmd = self.cmd_template.format(opts=opts, js_file=js_file)

        return {
            'name': js_file,
            'actions': [cmd],
            'file_dep': [config_file, js_file],
            }


    def tasks(self, patterns, group='all', exclude=(), options=None):
        """yield tasks as given by pattern

        @param group: (str) name of a group
        @param pattern: (list - str) list of path patterns of files to be linted
        @param exclude: (list - str) list of path of files to be removed
                        from selection
        @param options: (dict) extra options for group
        """

        # It seems jshint won't ever accept options from command line
        # https://github.com/jshint/jshint/issues/807
        # So we create a jshint config file for each "group"
        cfg = ConfigDict(copy.deepcopy(self._config))
        if options:
            cfg.merge(options)
        # FIXME do generate another hint.json file for 'all' group if
        # no options given
        config_file = '_hint_{}.json'.format(group)
        def write_config():
            with open(config_file, 'w') as fp:
                json.dump(cfg, fp, indent=4, sort_keys=True)
        yield {
            'name': config_file,
            'actions': [write_config],
            'targets': [config_file],
            'uptodate': [config_changed(cfg)],
            }

        # yield a task for every js file in selection
        base = Path('.')
        excluded = set([base.joinpath(e) for e in exclude])
        for pattern in patterns:
            for src in base.glob(pattern):
                # FIXME add a exclude pattern to __init__
                if src.match('.#*'): # emacs tmp files
                    continue
                if src not in excluded:
                    yield self(config_file, str(src))
