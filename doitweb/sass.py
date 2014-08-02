import glob
import os.path

from doitcmd import BaseCommand


class SASS(BaseCommand):
    cmd_template = 'sass {opts} {scss} {css}'
    base_options = {'style': 'expanded',
                    'unix-newlines': True}

    def __init__(self, **opts):
        """
        @param config: (str) config path
        """
        super(SASS, self).__init__(options=opts)


    def __call__(self, scss, css, all_source=None):
        """compile SASS file into CSS"""
        opts = self.opt_str(self.options)
        cmd = self.cmd_template.format(opts=opts, scss=scss, css=css)

        # The correct thing would be to parse the scss file
        # and get all included files.
        # Usually it's all scss files in the folder...
        if all_source is None:
            sass_folder = os.path.dirname(scss)
            all_source = glob.glob(sass_folder + '/*.scss')

        yield {
            'basename': 'sass',
            'name': css,
            'actions': [cmd],
            'file_dep': all_source,
            'targets': [css],
            }


# short-cut
def sass(scss_file, css_file):
    return SASS()(scss_file, css_file)

