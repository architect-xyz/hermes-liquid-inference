from typing import Any

from providers import register_provider
from providers.base import ProviderProfile


class ArchitectProfile(ProviderProfile):
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


# Releases before 0.4.0 registered the provider `liquid` and read
# LIQUID_API_KEY. The aliases keep `model.provider liquid` working, and Hermes
# reads LIQUID_API_KEY when ARCHITECT_API_KEY is not set.
register_provider(
    ArchitectProfile(
        name="architect",
        aliases=("architect-inference", "liquid", "liquid-inference"),
        display_name="Architect Inference",
        description="Architect Inference: an auction exchange for LLM inference",
        signup_url="https://inference.ai.exchange",
        env_vars=("ARCHITECT_API_KEY", "LIQUID_API_KEY", "ARCHITECT_BASE_URL"),
        base_url="https://router.inference.ai.exchange/v1",
        auth_type="api_key",
        default_headers={"X-Title": "Hermes Agent", "x-architect-cap-usd": "1.00"},
        default_aux_model="architect.auto",
        fallback_models=("architect.auto",),
    )
)
