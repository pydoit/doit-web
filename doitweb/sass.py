import glob
import os.path

def sass(scss_file, css_file):
    cmd = 'sass --style=expanded --unix-newlines {scss} {css}'
    sass_folder = os.path.dirname(scss_file)
    return {
        'name': css_file,
        'actions': [cmd.format(scss=scss_file, css=css_file)],
        'file_dep': glob.glob(sass_folder + '/*.scss'),
        'targets': [css_file],
        'verbosity': 2,
        }

