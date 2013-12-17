import json
import copy

from pathlib import Path
from mergedict import ConfigDict



class JsHint:
    def __init__(self, config=None):
        """
        @param config: (str) config path
        """
        if config:
            with open(config, 'r') as fp:
                self._config = ConfigDict(json.load(fp))
        else:
            self._config = {}

    def __call__(self, config_file, js_file):
        """return task metada to jshint single file"""
        return {
            'name': js_file,
            'actions': ['jshint --config {} {}'.format(config_file, js_file)],
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
        config_file = '_hint_{}.json'.format(group)
        with open(config_file, 'w') as fp:
            json.dump(cfg, fp, indent=4, sort_keys=True)

        # yield a task for every js file in selection
        base = Path('.')
        excluded = set([base.joinpath(e) for e in exclude])
        for pattern in patterns:
            for src in base.glob(pattern):
                if src not in excluded:
                    yield self(config_file, str(src))
