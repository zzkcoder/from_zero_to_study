'''### 数据结构建模题

* 要求

* 使用 `dataclass` 定义以下 5 个数据结构：

  - `Document`
  - `User`
  - `Message`
  - `Tool`
  - `AgentState`

  要求：

  1. `Document` 至少包含：文档 id、内容、来源、metadata、embedding。
  2. `User` 至少包含：用户 id、姓名、角色列表。
  3. `Message` 至少包含：角色、内容、名称、工具调用、工具调用 id。
  4. `Tool` 至少包含：工具名、描述、参数 schema、可调用函数。
  5. `AgentState` 至少包含：当前用户、消息列表、文档列表、工具列表、scratchpad、当前步数、最大步数、是否完成、错误信息。
  6. 所有可变默认值必须使用 `field(default_factory=...)`，不能写 `= []` 或 `= {}`。
  7. 写完后解释：为什么 `AgentState` 里需要 `messages`、`documents`、`tools`、`scratchpad`、`step`、`done`？'''

from dadtaclasses import dataclass,field
from typing import Any, Literal, Callable

@dataclass
class Document:
    id:str
    content:str
    cource:str|None=None  
    metadata:dict[str,Any]=field(default_factory=dict)
    embedding:list[float] |None=None
 
@dataclass
class User:
    id: str
    name: str
    roles: list[str] = field(default_factory=list)


@dataclass
class ToolCall:
    id: str
    name: str
    arguments: dict[str, Any] = field(default_factory=dict)


@dataclass
class Message:
    role: Literal["system", "user", "assistant", "tool"]
    content: str
    name: str | None = None
    tool_calls: list[ToolCall] = field(default_factory=list)
    tool_call_id: str | None = None


@dataclass
class Tool:
    name: str
    description: str
    parameters: dict[str, Any] = field(default_factory=dict)
    func: Callable[..., Any] | None = None


@dataclass
class AgentState:
    user: User
    messages: list[Message] = field(default_factory=list)  #放的是按照 Message 模板造出来的实例
    documents: list[Document] = field(default_factory=list)
    tools: list[Tool] = field(default_factory=list)
    scratchpad: dict[str, Any] = field(default_factory=dict)
    step: int = 0
    max_steps: int = 10
    done: bool = False
    error: str | None = None