from pydantic import BaseModel, Field


class NotebookLMNotebookResponse(BaseModel):
    id: str
    title: str
    created_at: str | None = None
    sources_count: int = 0
    is_owner: bool = True


class NotebookLMReferenceResponse(BaseModel):
    source_id: str
    citation_number: int | None = None
    cited_text: str | None = None
    source_title: str | None = None
    source_url: str | None = None


class NotebookLMAskRequest(BaseModel):
    notebook_id: str = Field(..., title="ID блокнота NotebookLM")
    question: str = Field(..., title="Вопрос")
    source_ids: list[str] | None = Field(default=None, title="Ограничение по source_id")
    conversation_id: str | None = Field(default=None, title="ID диалога")


class NotebookLMAskResponse(BaseModel):
    notebook_id: str
    answer: str
    conversation_id: str
    turn_number: int
    is_follow_up: bool
    references: list[NotebookLMReferenceResponse]


class NotebookLMBatchAskRequest(BaseModel):
    notebook_ids: list[str] = Field(..., min_length=1, title="Список ID блокнотов")
    question: str = Field(..., title="Вопрос")


class NotebookLMBatchAskResponse(BaseModel):
    question: str
    results: list[NotebookLMAskResponse]
    merged_answer: str


class NotebookLMHealthResponse(BaseModel):
    success: bool
    authenticated: bool
    storage_path: str
    browser_profile_dir: str
    notebook_count: int | None = None
    error: str | None = None


class NotebookLMReauthRequest(BaseModel):
    timeout_seconds: int | None = Field(default=None, gt=0, le=900)
    headless: bool | None = None


class NotebookLMReauthResponse(BaseModel):
    success: bool
    storage_path: str
    browser_profile_dir: str
    current_url: str | None = None
    authenticated: bool
    error: str | None = None
