# Liquid Inference for Hermes Agent

Adds [Liquid Inference](https://inference.ai.exchange) to
[Hermes Agent](https://github.com/NousResearch/hermes-agent) as a model provider.

## Requirements

- Hermes Agent 0.21.6 or later.
- A Liquid Inference buyer key with the `spend` scope.

## Install

```bash
hermes plugins install architect-xyz/hermes-liquid-inference --enable
```

The command asks for `LIQUID_API_KEY` and saves it in `~/.hermes/.env`.

## Configure

```bash
hermes config set model.provider liquid
hermes config set model.default liquid.auto
```

Each request has a cap of 1 USD. To change the cap:

```bash
hermes config set model.default_headers.x-liquid-cap-usd 0.25
```

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
