# Contributing

## Requirements

- [Poetry][poetry]
- [npm][npm]
- [addlicense][addlicense]

## Install

```shell
poetry install
```

## Analyze (format, lint)

```shell
poetry shell
nox -t analyze
```

## Docs

Be sure to update the [README](./README.md) if necessary.

<!-- markdownlint-disable line-length -->

[poetry]: https://python-poetry.org/docs/#installation
[npm]: https://docs.npmjs.com/downloading-and-installing-node-js-and-npm
[addlicense]: https://github.com/google/addlicense
