"""install bower(http://bower.io) packages

bower packages specified in bower.json are downloaded into
folder `bower_components`.
Copy package files into a destination folder.
"""

from configclass import Config



def bower(file_map, config=None):
    """create bower tasks

    @param file_map: dict with destination file: source i.e.
                     {'chai.js': 'chai/chai.js',
                      'polymer-platform.js': 'polymer-platform/platform.js'}
    """
    default_config = Config(components_dir='components')
    config = default_config.make(config)

    # download packages
    yield {
        'basename': 'bower',
        'name': 'install',
        'actions': ['bower install'],
        'file_dep': ['bower.json'],
        'targets': ['bower_components'],
        }

    # create destination folder
    yield {
        'basename': 'bower',
        'name': config['components_dir'],
        'actions': ['mkdir -p {}'.format(config['components_dir'])],
        }

    # copy mapped files into destination static folder
    for dst, src in file_map.items():
        yield {
            'basename': 'bower',
            'name': dst,
            'actions': ['cp %(dependencies)s %(targets)s'],
            'file_dep': ['bower_components/{}'.format(src)],
            'targets': ['{}/{}'.format(config['components_dir'], dst)],
            }
