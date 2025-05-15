# Publishing snp2str to PyPI

This document outlines the steps to publish the snp2str package to PyPI.

## Prerequisites

1. Create accounts on PyPI and Test PyPI:
   - PyPI: https://pypi.org/account/register/
   - Test PyPI: https://test.pypi.org/account/register/

2. Install required tools (already installed in your virtual environment):
   - build: For building the package
   - twine: For uploading the package to PyPI

## Build the Package

1. Activate your virtual environment:
   ```bash
   source venv/bin/activate
   ```

2. Build the distribution packages:
   ```bash
   python -m build
   ```

   This will create the following files in the `dist/` directory:
   - `snp2str-0.1.tar.gz`: Source distribution
   - `snp2str-0.1-py3-none-any.whl`: Wheel distribution

## Test Your Package (Optional but Recommended)

1. Upload to Test PyPI first:
   ```bash
   python -m twine upload --repository testpypi dist/*
   ```

2. Test the installation from Test PyPI:
   ```bash
   python -m pip install --index-url https://test.pypi.org/simple/ --no-deps snp2str
   ```

3. Verify that the package works correctly.

## Publish to PyPI

Once you've confirmed everything works correctly, publish to the real PyPI:

```bash
python -m twine upload dist/*
```

## Version Bumping for Future Releases

When you need to release a new version:

1. Update the version number in:
   - `snp2str/__init__.py`
   - `setup.py` (if needed)

2. Create a Git tag (optional):
   ```bash
   git tag -a v0.1.1 -m "Release version 0.1.1"
   git push origin v0.1.1
   ```

3. Build and upload the new package following the steps above.

## Maintenance

- Keep your PyPI credentials secure
- Update the README.md when adding new features
- Add unit tests for new functionality
- Consider setting up continuous integration for automated testing and deployment