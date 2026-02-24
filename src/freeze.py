"""Frozen-Flask build script.

Renders all Flask routes to static HTML files for deployment
to GitHub Pages (or any static file host).

Usage:
  cd src/
  python freeze.py
"""

import os
import shutil

from bookshelf import app
from flask_frozen import Freezer

# Tell the app not to apply Talisman/Compress during freezing
os.environ['FLASK_FREEZE'] = '1'
# Use production path for content.json loading
os.environ['FLASK_ENV'] = 'production'

# Configure the build output directory
BUILD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'build')
app.config['FREEZER_DESTINATION'] = BUILD_DIR

# Multi-domain support via environment override
# If GH_PAGES_BASE_URL is set, generate absolute URLs from that base.
# Otherwise, generate relative URLs for maximum compatibility across domains.
ENV_BASE_URL = os.environ.get('GH_PAGES_BASE_URL')
if ENV_BASE_URL:
    app.config['FREEZER_BASE_URL'] = ENV_BASE_URL
    app.config['FREEZER_RELATIVE_URLS'] = False
else:
    app.config['FREEZER_RELATIVE_URLS'] = True

app.config['FREEZER_REMOVE_EXTRA_FILES'] = True

freezer = Freezer(app)


@freezer.register_generator
def essay_urls():
    """Generate URLs for all essay pages."""
    essays = [
        'pump-station-operators-individual',
        'pump-station-operators-team',
        'what-does-a-pump-station-do',
        'keeping-the-pumps-running',
        'day-after-a-storm',
        'evening-at-station-d',
        'challenges',
        'watch-morning',
        'water-creatures',
    ]
    for title in essays:
        yield '/essay/{}/'.format(title)


@freezer.register_generator
def gallery_urls():
    """Generate URLs for all gallery pages."""
    galleries = [
        'water-series',
        'behind-the-scenes',
    ]
    for series in galleries:
        yield '/gallery/{}/'.format(series)


def copy_extras():
    """Copy extra files into the build directory (404, etc.)."""
    extras_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'extras')
    notfound_src = os.path.join(extras_dir, '404.html')
    if os.path.exists(notfound_src):
        shutil.copy2(notfound_src, os.path.join(BUILD_DIR, '404.html'))
        print('  Copied 404.html')

    # Conditional CNAME: only write if using a custom domain (not the default github.io)
    write_cname = False
    if ENV_BASE_URL:
        if not ENV_BASE_URL.endswith('.github.io'):
            write_cname = True
    if write_cname:
        cname_path = os.path.join(BUILD_DIR, 'CNAME')
        with open(cname_path, 'w') as f:
            f.write(ENV_BASE_URL.rstrip('/') + '\n')
        print('  Wrote CNAME: {}'.format(ENV_BASE_URL))


if __name__ == '__main__':
    print('Freezing site...')
    freezer.freeze()
    print('Frozen successfully to: {}'.format(BUILD_DIR))

    print('Copying extras...')
    copy_extras()

    print('Done! Static site is ready in: {}'.format(BUILD_DIR))
