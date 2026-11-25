# Architect Inference for Hermes Agent

Adds [Architect Inference](https://inference.ai.exchange) to
[Hermes Agent](https://github.com/NousResearch/hermes-agent) as a model provider.

## Requirements

- Hermes Agent 0.21.6 or later.
- An Architect Inference buyer key with the `spend` scope.

## Install

```bash
hermes plugins install architect-xyz/hermes-liquid-inference --enable
```

The command asks for `ARCHITECT_API_KEY` and saves it in `~/.hermes/.env`.

## Configure

```bash
hermes config set model.provider architect
hermes config set model.default architect.auto
```

Each request has a cap of 1 USD. To change the cap:

```bash
hermes config set model.default_headers.x-architect-cap-usd 0.25
```

To use an exchange other than the production exchange, set
`ARCHITECT_BASE_URL` to its URL, with `/v1`.

## Reasoning effort

Task requests use `medium` when you do not set a reasoning effort. To select
another level:

```bash
hermes config set agent.reasoning_effort high
```

If you select `none` or turn reasoning off, the plugin sends no reasoning
effort. Auxiliary requests do not use the task default.

If no offer accepts the effort, the exchange refuses the request with
`400 unsupported_parameter` and makes no charge. Hermes then sends the request
again without the effort.

## Upgrade from 0.3 or earlier

Releases before 0.4.0 used the Liquid Inference names. Version 0.4.0 accepts
the old names, so you do not have to change your configuration:

| Old name                                  | New name                                     | After the upgrade                                  |
| ----------------------------------------- | -------------------------------------------- | -------------------------------------------------- |
| `model.provider liquid`                   | `model.provider architect`                   | `liquid` and `liquid-inference` are aliases.       |
| `LIQUID_API_KEY`                          | `ARCHITECT_API_KEY`                          | Hermes reads `LIQUID_API_KEY` when the new name is not set. |
| `liquid.auto`                             | `architect.auto`                             | The exchange accepts both names.                   |
| `model.default_headers.x-liquid-cap-usd`  | `model.default_headers.x-architect-cap-usd`  | The exchange uses the lower of the two caps.       |
| `LIQUID_BASE_URL`                         | `ARCHITECT_BASE_URL`                         | Hermes reads only the new name. Rename it.         |
