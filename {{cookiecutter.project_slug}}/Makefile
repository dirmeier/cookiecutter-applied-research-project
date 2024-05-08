PKG_VERSION=`hatch version`

tag:
	git tag -a v${PKG_VERSION} -m v${PKG_VERSION}
	git push --tag

format:
    tox -e format

check:
    tox -e lints,types

test:
    tox -e tests
