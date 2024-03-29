from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Optional

__all__ = [
    "IntegrationRuntimeSpec",
    "METADATA_COMMON_RUN_AS_PARTY",
    "METADATA_INTEGRATION_COMMENT",
    "METADATA_INTEGRATION_ENABLED",
    "METADATA_INTEGRATION_ID",
    "METADATA_INTEGRATION_RUNTIME",
    "METADATA_INTEGRATION_RUN_AS_PARTY",
    "METADATA_INTEGRATION_TYPE_ID",
    "METADATA_TRIGGER_NAME",
]

METADATA_COMMON_RUN_AS_PARTY = "runAs"
METADATA_TRIGGER_NAME = "triggerName"

METADATA_INTEGRATION_ID = "com.projectdabl.integrations.integrationId"
METADATA_INTEGRATION_TYPE_ID = "com.projectdabl.integrations.integrationTypeId"
METADATA_INTEGRATION_COMMENT = "com.projectdabl.integrations.comment"
METADATA_INTEGRATION_ENABLED = "com.projectdabl.integrations.enabled"
METADATA_INTEGRATION_RUN_AS_PARTY = "com.projectdabl.integrations.runAsParty"
METADATA_INTEGRATION_RUNTIME = "com.projectdabl.integrations.runtime"


@dataclass(frozen=True)
class IntegrationRuntimeSpec:
    type_id: Optional[str]
    metadata: Mapping[str, str]
