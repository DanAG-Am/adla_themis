from dataclasses import dataclass, field


@dataclass
class AgentIntent:

    skill: str
    brand: str
    dimensions: list[str] = field(default_factory=list)
    metrics: list[str] = field(default_factory=list)
    limit: int = 10