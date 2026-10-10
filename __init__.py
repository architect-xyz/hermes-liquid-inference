from typing import Any

from providers import register_provider
from providers.base import ProviderProfile


class LiquidProfile(ProviderProfile):
    # Use the task default of the custom provider. This hook also lets Hermes
    # omit the effort after a refusal, and leaves auxiliary requests unchanged.
    def default_reasoning_config(self, model: str | None = None) -> dict | None:
        return {"enabled": True, "effort": "medium"}

    def build_api_kwargs_extras(
        self, *, reasoning_config: dict | None = None, **context: Any
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        config = reasoning_config or {}
        effort = config.get("effort")
        if not effort or effort == "none" or config.get("enabled") is False:
            return {}, {}
        return {}, {"reasoning_effort": effort}


register_provider(
    LiquidProfile(
        name="liquid",
        aliases=("liquid-inference",),
        display_name="Liquid Inference",
        description="Liquid Inference: an auction exchange for LLM inference",
        signup_url="https://inference.ai.exchange",
        env_vars=("LIQUID_API_KEY", "LIQUID_BASE_URL"),
        base_url="https://router.inference.ai.exchange/v1",
        auth_type="api_key",
        default_headers={"X-Title": "Hermes Agent", "x-liquid-cap-usd": "1.00"},
        default_aux_model="liquid.auto",
        fallback_models=("liquid.auto",),
    )
)
