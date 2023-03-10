
# Cleanup folders from previous build
if [ -d ./build ]; then rm -Rf ./build; fi
if [ -d ./dist ]; then rm -Rf ./dist; fi

# Build
pyinstaller run.py

# Add extra files (not covered by pyinstaller)
cp ./config.py ./dist/run/config.py
cp --verbose -r ./migrations ./dist/run/migrations
mkdir ./dist/run/app
cp --verbose -r ./app/static ./dist/run/app/static
cp --verbose -r ./app/templates ./dist/run/app/templates
cp --verbose -r ./app/translations ./dist/run/app/translations
