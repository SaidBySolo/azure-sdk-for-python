# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import sys
from typing import Any, Dict, List, Optional, TYPE_CHECKING, Union

from .. import _serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models
if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object


class AnswersFromTextOptions(_serialization.Model):
    """The question and text record parameters to answer.

    All required parameters must be populated in order to send to Azure.

    :ivar question: User question to query against the given text records. Required.
    :vartype question: str
    :ivar text_documents: Text records to be searched for given question. Required.
    :vartype text_documents: list[~azure.ai.language.questionanswering.models.TextDocument]
    :ivar language: Language of the text records. This is BCP-47 representation of a language. For
     example, use "en" for English; "es" for Spanish etc. If not set, use "en" for English as
     default.
    :vartype language: str
    """

    _validation = {
        "question": {"required": True},
        "text_documents": {"required": True},
    }

    _attribute_map = {
        "question": {"key": "question", "type": "str"},
        "text_documents": {"key": "records", "type": "[TextDocument]"},
        "language": {"key": "language", "type": "str"},
    }

    def __init__(
        self, *, question: str, text_documents: List["_models.TextDocument"], language: Optional[str] = None, **kwargs
    ):
        """
        :keyword question: User question to query against the given text records. Required.
        :paramtype question: str
        :keyword text_documents: Text records to be searched for given question. Required.
        :paramtype text_documents: list[~azure.ai.language.questionanswering.models.TextDocument]
        :keyword language: Language of the text records. This is BCP-47 representation of a language.
         For example, use "en" for English; "es" for Spanish etc. If not set, use "en" for English as
         default.
        :paramtype language: str
        """
        super().__init__(**kwargs)
        self.question = question
        self.text_documents = text_documents
        self.language = language


class AnswersFromTextResult(_serialization.Model):
    """Represents the answer results.

    :ivar answers: Represents the answer results.
    :vartype answers: list[~azure.ai.language.questionanswering.models.TextAnswer]
    """

    _attribute_map = {
        "answers": {"key": "answers", "type": "[TextAnswer]"},
    }

    def __init__(self, *, answers: Optional[List["_models.TextAnswer"]] = None, **kwargs):
        """
        :keyword answers: Represents the answer results.
        :paramtype answers: list[~azure.ai.language.questionanswering.models.TextAnswer]
        """
        super().__init__(**kwargs)
        self.answers = answers


class AnswersOptions(_serialization.Model):
    """Parameters to query a knowledge base.

    :ivar qna_id: Exact QnA ID to fetch from the knowledge base, this field takes priority over
     question.
    :vartype qna_id: int
    :ivar question: User question to query against the knowledge base.
    :vartype question: str
    :ivar top: Max number of answers to be returned for the question.
    :vartype top: int
    :ivar user_id: Unique identifier for the user.
    :vartype user_id: str
    :ivar confidence_threshold: Minimum threshold score for answers, value ranges from 0 to 1.
    :vartype confidence_threshold: float
    :ivar answer_context: Context object with previous QnA's information.
    :vartype answer_context: ~azure.ai.language.questionanswering.models.KnowledgeBaseAnswerContext
    :ivar ranker_kind: Type of ranker to be used.
    :vartype ranker_kind: str
    :ivar filters: Filter QnAs based on given metadata list and knowledge base sources.
    :vartype filters: ~azure.ai.language.questionanswering.models.QueryFilters
    :ivar short_answer_options: To configure Answer span prediction feature.
    :vartype short_answer_options: ~azure.ai.language.questionanswering.models.ShortAnswerOptions
    :ivar include_unstructured_sources: (Optional) Flag to enable Query over Unstructured Sources.
    :vartype include_unstructured_sources: bool
    """

    _validation = {
        "confidence_threshold": {"maximum": 1, "minimum": 0},
    }

    _attribute_map = {
        "qna_id": {"key": "qnaId", "type": "int"},
        "question": {"key": "question", "type": "str"},
        "top": {"key": "top", "type": "int"},
        "user_id": {"key": "userId", "type": "str"},
        "confidence_threshold": {"key": "confidenceScoreThreshold", "type": "float"},
        "answer_context": {"key": "context", "type": "KnowledgeBaseAnswerContext"},
        "ranker_kind": {"key": "rankerType", "type": "str"},
        "filters": {"key": "filters", "type": "QueryFilters"},
        "short_answer_options": {"key": "answerSpanRequest", "type": "ShortAnswerOptions"},
        "include_unstructured_sources": {"key": "includeUnstructuredSources", "type": "bool"},
    }

    def __init__(
        self,
        *,
        qna_id: Optional[int] = None,
        question: Optional[str] = None,
        top: Optional[int] = None,
        user_id: Optional[str] = None,
        confidence_threshold: Optional[float] = None,
        answer_context: Optional["_models.KnowledgeBaseAnswerContext"] = None,
        ranker_kind: Optional[str] = None,
        filters: Optional["_models.QueryFilters"] = None,
        short_answer_options: Optional["_models.ShortAnswerOptions"] = None,
        include_unstructured_sources: Optional[bool] = None,
        **kwargs
    ):
        """
        :keyword qna_id: Exact QnA ID to fetch from the knowledge base, this field takes priority over
         question.
        :paramtype qna_id: int
        :keyword question: User question to query against the knowledge base.
        :paramtype question: str
        :keyword top: Max number of answers to be returned for the question.
        :paramtype top: int
        :keyword user_id: Unique identifier for the user.
        :paramtype user_id: str
        :keyword confidence_threshold: Minimum threshold score for answers, value ranges from 0 to 1.
        :paramtype confidence_threshold: float
        :keyword answer_context: Context object with previous QnA's information.
        :paramtype answer_context:
         ~azure.ai.language.questionanswering.models.KnowledgeBaseAnswerContext
        :keyword ranker_kind: Type of ranker to be used.
        :paramtype ranker_kind: str
        :keyword filters: Filter QnAs based on given metadata list and knowledge base sources.
        :paramtype filters: ~azure.ai.language.questionanswering.models.QueryFilters
        :keyword short_answer_options: To configure Answer span prediction feature.
        :paramtype short_answer_options: ~azure.ai.language.questionanswering.models.ShortAnswerOptions
        :keyword include_unstructured_sources: (Optional) Flag to enable Query over Unstructured
         Sources.
        :paramtype include_unstructured_sources: bool
        """
        super().__init__(**kwargs)
        self.qna_id = qna_id
        self.question = question
        self.top = top
        self.user_id = user_id
        self.confidence_threshold = confidence_threshold
        self.answer_context = answer_context
        self.ranker_kind = ranker_kind
        self.filters = filters
        self.short_answer_options = short_answer_options
        self.include_unstructured_sources = include_unstructured_sources


class AnswerSpan(_serialization.Model):
    """Answer span object of QnA.

    :ivar text: Predicted text of answer span.
    :vartype text: str
    :ivar confidence: Predicted score of answer span, value ranges from 0 to 1.
    :vartype confidence: float
    :ivar offset: The answer span offset from the start of answer.
    :vartype offset: int
    :ivar length: The length of the answer span.
    :vartype length: int
    """

    _validation = {
        "confidence": {"maximum": 1, "minimum": 0},
    }

    _attribute_map = {
        "text": {"key": "text", "type": "str"},
        "confidence": {"key": "confidenceScore", "type": "float"},
        "offset": {"key": "offset", "type": "int"},
        "length": {"key": "length", "type": "int"},
    }

    def __init__(
        self,
        *,
        text: Optional[str] = None,
        confidence: Optional[float] = None,
        offset: Optional[int] = None,
        length: Optional[int] = None,
        **kwargs
    ):
        """
        :keyword text: Predicted text of answer span.
        :paramtype text: str
        :keyword confidence: Predicted score of answer span, value ranges from 0 to 1.
        :paramtype confidence: float
        :keyword offset: The answer span offset from the start of answer.
        :paramtype offset: int
        :keyword length: The length of the answer span.
        :paramtype length: int
        """
        super().__init__(**kwargs)
        self.text = text
        self.confidence = confidence
        self.offset = offset
        self.length = length


class AnswersResult(_serialization.Model):
    """Represents List of Question Answers.

    :ivar answers: Represents Answer Result list.
    :vartype answers: list[~azure.ai.language.questionanswering.models.KnowledgeBaseAnswer]
    """

    _attribute_map = {
        "answers": {"key": "answers", "type": "[KnowledgeBaseAnswer]"},
    }

    def __init__(self, *, answers: Optional[List["_models.KnowledgeBaseAnswer"]] = None, **kwargs):
        """
        :keyword answers: Represents Answer Result list.
        :paramtype answers: list[~azure.ai.language.questionanswering.models.KnowledgeBaseAnswer]
        """
        super().__init__(**kwargs)
        self.answers = answers


class Error(_serialization.Model):
    """The error object.

    All required parameters must be populated in order to send to Azure.

    :ivar code: One of a server-defined set of error codes. Required. Known values are:
     "InvalidRequest", "InvalidArgument", "Unauthorized", "Forbidden", "NotFound",
     "ProjectNotFound", "OperationNotFound", "AzureCognitiveSearchNotFound",
     "AzureCognitiveSearchIndexNotFound", "TooManyRequests", "AzureCognitiveSearchThrottling",
     "AzureCognitiveSearchIndexLimitReached", "InternalServerError", and "ServiceUnavailable".
    :vartype code: str or ~azure.ai.language.questionanswering.models.ErrorCode
    :ivar message: A human-readable representation of the error. Required.
    :vartype message: str
    :ivar target: The target of the error.
    :vartype target: str
    :ivar details: An array of details about specific errors that led to this reported error.
    :vartype details: list[~azure.ai.language.questionanswering.models.Error]
    :ivar innererror: An object containing more specific information than the current object about
     the error.
    :vartype innererror: ~azure.ai.language.questionanswering.models.InnerErrorModel
    """

    _validation = {
        "code": {"required": True},
        "message": {"required": True},
    }

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
        "target": {"key": "target", "type": "str"},
        "details": {"key": "details", "type": "[Error]"},
        "innererror": {"key": "innererror", "type": "InnerErrorModel"},
    }

    def __init__(
        self,
        *,
        code: Union[str, "_models.ErrorCode"],
        message: str,
        target: Optional[str] = None,
        details: Optional[List["_models.Error"]] = None,
        innererror: Optional["_models.InnerErrorModel"] = None,
        **kwargs
    ):
        """
        :keyword code: One of a server-defined set of error codes. Required. Known values are:
         "InvalidRequest", "InvalidArgument", "Unauthorized", "Forbidden", "NotFound",
         "ProjectNotFound", "OperationNotFound", "AzureCognitiveSearchNotFound",
         "AzureCognitiveSearchIndexNotFound", "TooManyRequests", "AzureCognitiveSearchThrottling",
         "AzureCognitiveSearchIndexLimitReached", "InternalServerError", and "ServiceUnavailable".
        :paramtype code: str or ~azure.ai.language.questionanswering.models.ErrorCode
        :keyword message: A human-readable representation of the error. Required.
        :paramtype message: str
        :keyword target: The target of the error.
        :paramtype target: str
        :keyword details: An array of details about specific errors that led to this reported error.
        :paramtype details: list[~azure.ai.language.questionanswering.models.Error]
        :keyword innererror: An object containing more specific information than the current object
         about the error.
        :paramtype innererror: ~azure.ai.language.questionanswering.models.InnerErrorModel
        """
        super().__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = target
        self.details = details
        self.innererror = innererror


class ErrorResponse(_serialization.Model):
    """Error response.

    :ivar error: The error object.
    :vartype error: ~azure.ai.language.questionanswering.models.Error
    """

    _attribute_map = {
        "error": {"key": "error", "type": "Error"},
    }

    def __init__(self, *, error: Optional["_models.Error"] = None, **kwargs):
        """
        :keyword error: The error object.
        :paramtype error: ~azure.ai.language.questionanswering.models.Error
        """
        super().__init__(**kwargs)
        self.error = error


class InnerErrorModel(_serialization.Model):
    """An object containing more specific information about the error. As per Microsoft One API guidelines -
    https://github.com/Microsoft/api-guidelines/blob/vNext/Guidelines.md#7102-error-condition-responses.

    All required parameters must be populated in order to send to Azure.

    :ivar code: One of a server-defined set of error codes. Required. Known values are:
     "InvalidRequest", "InvalidParameterValue", "KnowledgeBaseNotFound",
     "AzureCognitiveSearchNotFound", "AzureCognitiveSearchThrottling", and "ExtractionFailure".
    :vartype code: str or ~azure.ai.language.questionanswering.models.InnerErrorCode
    :ivar message: Error message. Required.
    :vartype message: str
    :ivar details: Error details.
    :vartype details: dict[str, str]
    :ivar target: Error target.
    :vartype target: str
    :ivar innererror: An object containing more specific information than the current object about
     the error.
    :vartype innererror: ~azure.ai.language.questionanswering.models.InnerErrorModel
    """

    _validation = {
        "code": {"required": True},
        "message": {"required": True},
    }

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
        "details": {"key": "details", "type": "{str}"},
        "target": {"key": "target", "type": "str"},
        "innererror": {"key": "innererror", "type": "InnerErrorModel"},
    }

    def __init__(
        self,
        *,
        code: Union[str, "_models.InnerErrorCode"],
        message: str,
        details: Optional[Dict[str, str]] = None,
        target: Optional[str] = None,
        innererror: Optional["_models.InnerErrorModel"] = None,
        **kwargs
    ):
        """
        :keyword code: One of a server-defined set of error codes. Required. Known values are:
         "InvalidRequest", "InvalidParameterValue", "KnowledgeBaseNotFound",
         "AzureCognitiveSearchNotFound", "AzureCognitiveSearchThrottling", and "ExtractionFailure".
        :paramtype code: str or ~azure.ai.language.questionanswering.models.InnerErrorCode
        :keyword message: Error message. Required.
        :paramtype message: str
        :keyword details: Error details.
        :paramtype details: dict[str, str]
        :keyword target: Error target.
        :paramtype target: str
        :keyword innererror: An object containing more specific information than the current object
         about the error.
        :paramtype innererror: ~azure.ai.language.questionanswering.models.InnerErrorModel
        """
        super().__init__(**kwargs)
        self.code = code
        self.message = message
        self.details = details
        self.target = target
        self.innererror = innererror


class KnowledgeBaseAnswer(_serialization.Model):
    """Represents knowledge base answer.

    :ivar questions: List of questions associated with the answer.
    :vartype questions: list[str]
    :ivar answer: Answer text.
    :vartype answer: str
    :ivar confidence: Answer confidence score, value ranges from 0 to 1.
    :vartype confidence: float
    :ivar qna_id: ID of the QnA result.
    :vartype qna_id: int
    :ivar source: Source of QnA result.
    :vartype source: str
    :ivar metadata: Metadata associated with the answer, useful to categorize or filter question
     answers.
    :vartype metadata: dict[str, str]
    :ivar dialog: Dialog associated with Answer.
    :vartype dialog: ~azure.ai.language.questionanswering.models.KnowledgeBaseAnswerDialog
    :ivar short_answer: Answer span object of QnA with respect to user's question.
    :vartype short_answer: ~azure.ai.language.questionanswering.models.AnswerSpan
    """

    _validation = {
        "confidence": {"maximum": 1, "minimum": 0},
    }

    _attribute_map = {
        "questions": {"key": "questions", "type": "[str]"},
        "answer": {"key": "answer", "type": "str"},
        "confidence": {"key": "confidenceScore", "type": "float"},
        "qna_id": {"key": "id", "type": "int"},
        "source": {"key": "source", "type": "str"},
        "metadata": {"key": "metadata", "type": "{str}"},
        "dialog": {"key": "dialog", "type": "KnowledgeBaseAnswerDialog"},
        "short_answer": {"key": "answerSpan", "type": "AnswerSpan"},
    }

    def __init__(
        self,
        *,
        questions: Optional[List[str]] = None,
        answer: Optional[str] = None,
        confidence: Optional[float] = None,
        qna_id: Optional[int] = None,
        source: Optional[str] = None,
        metadata: Optional[Dict[str, str]] = None,
        dialog: Optional["_models.KnowledgeBaseAnswerDialog"] = None,
        short_answer: Optional["_models.AnswerSpan"] = None,
        **kwargs
    ):
        """
        :keyword questions: List of questions associated with the answer.
        :paramtype questions: list[str]
        :keyword answer: Answer text.
        :paramtype answer: str
        :keyword confidence: Answer confidence score, value ranges from 0 to 1.
        :paramtype confidence: float
        :keyword qna_id: ID of the QnA result.
        :paramtype qna_id: int
        :keyword source: Source of QnA result.
        :paramtype source: str
        :keyword metadata: Metadata associated with the answer, useful to categorize or filter question
         answers.
        :paramtype metadata: dict[str, str]
        :keyword dialog: Dialog associated with Answer.
        :paramtype dialog: ~azure.ai.language.questionanswering.models.KnowledgeBaseAnswerDialog
        :keyword short_answer: Answer span object of QnA with respect to user's question.
        :paramtype short_answer: ~azure.ai.language.questionanswering.models.AnswerSpan
        """
        super().__init__(**kwargs)
        self.questions = questions
        self.answer = answer
        self.confidence = confidence
        self.qna_id = qna_id
        self.source = source
        self.metadata = metadata
        self.dialog = dialog
        self.short_answer = short_answer


class KnowledgeBaseAnswerContext(_serialization.Model):
    """Context object with previous QnA's information.

    All required parameters must be populated in order to send to Azure.

    :ivar previous_qna_id: Previous turn top answer result QnA ID. Required.
    :vartype previous_qna_id: int
    :ivar previous_question: Previous user query.
    :vartype previous_question: str
    """

    _validation = {
        "previous_qna_id": {"required": True},
    }

    _attribute_map = {
        "previous_qna_id": {"key": "previousQnaId", "type": "int"},
        "previous_question": {"key": "previousUserQuery", "type": "str"},
    }

    def __init__(self, *, previous_qna_id: int, previous_question: Optional[str] = None, **kwargs):
        """
        :keyword previous_qna_id: Previous turn top answer result QnA ID. Required.
        :paramtype previous_qna_id: int
        :keyword previous_question: Previous user query.
        :paramtype previous_question: str
        """
        super().__init__(**kwargs)
        self.previous_qna_id = previous_qna_id
        self.previous_question = previous_question


class KnowledgeBaseAnswerDialog(_serialization.Model):
    """Dialog associated with Answer.

    :ivar is_context_only: To mark if a prompt is relevant only with a previous question or not. If
     true, do not include this QnA as search result for queries without context; otherwise, if
     false, ignores context and includes this QnA in search result.
    :vartype is_context_only: bool
    :ivar prompts: List of prompts associated with the answer.
    :vartype prompts: list[~azure.ai.language.questionanswering.models.KnowledgeBaseAnswerPrompt]
    """

    _validation = {
        "prompts": {"max_items": 20, "min_items": 0},
    }

    _attribute_map = {
        "is_context_only": {"key": "isContextOnly", "type": "bool"},
        "prompts": {"key": "prompts", "type": "[KnowledgeBaseAnswerPrompt]"},
    }

    def __init__(
        self,
        *,
        is_context_only: Optional[bool] = None,
        prompts: Optional[List["_models.KnowledgeBaseAnswerPrompt"]] = None,
        **kwargs
    ):
        """
        :keyword is_context_only: To mark if a prompt is relevant only with a previous question or not.
         If true, do not include this QnA as search result for queries without context; otherwise, if
         false, ignores context and includes this QnA in search result.
        :paramtype is_context_only: bool
        :keyword prompts: List of prompts associated with the answer.
        :paramtype prompts: list[~azure.ai.language.questionanswering.models.KnowledgeBaseAnswerPrompt]
        """
        super().__init__(**kwargs)
        self.is_context_only = is_context_only
        self.prompts = prompts


class KnowledgeBaseAnswerPrompt(_serialization.Model):
    """Prompt for an answer.

    :ivar display_order: Index of the prompt - used in ordering of the prompts.
    :vartype display_order: int
    :ivar qna_id: QnA ID corresponding to the prompt.
    :vartype qna_id: int
    :ivar display_text: Text displayed to represent a follow up question prompt.
    :vartype display_text: str
    """

    _validation = {
        "display_text": {"max_length": 200},
    }

    _attribute_map = {
        "display_order": {"key": "displayOrder", "type": "int"},
        "qna_id": {"key": "qnaId", "type": "int"},
        "display_text": {"key": "displayText", "type": "str"},
    }

    def __init__(
        self,
        *,
        display_order: Optional[int] = None,
        qna_id: Optional[int] = None,
        display_text: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword display_order: Index of the prompt - used in ordering of the prompts.
        :paramtype display_order: int
        :keyword qna_id: QnA ID corresponding to the prompt.
        :paramtype qna_id: int
        :keyword display_text: Text displayed to represent a follow up question prompt.
        :paramtype display_text: str
        """
        super().__init__(**kwargs)
        self.display_order = display_order
        self.qna_id = qna_id
        self.display_text = display_text


class MetadataFilter(_serialization.Model):
    """Find QnAs that are associated with the given list of metadata.

    :ivar metadata:
    :vartype metadata: list[JSON]
    :ivar logical_operation: Operation used to join metadata filters.
    :vartype logical_operation: str
    """

    _attribute_map = {
        "metadata": {"key": "metadata", "type": "[object]"},
        "logical_operation": {"key": "logicalOperation", "type": "str"},
    }

    def __init__(self, *, metadata: Optional[List[JSON]] = None, logical_operation: Optional[str] = None, **kwargs):
        """
        :keyword metadata:
        :paramtype metadata: list[JSON]
        :keyword logical_operation: Operation used to join metadata filters.
        :paramtype logical_operation: str
        """
        super().__init__(**kwargs)
        self.metadata = metadata
        self.logical_operation = logical_operation


class QueryFilters(_serialization.Model):
    """filters over knowledge base.

    :ivar metadata_filter: Find QnAs that are associated with the given list of metadata.
    :vartype metadata_filter: ~azure.ai.language.questionanswering.models.MetadataFilter
    :ivar source_filter: Find QnAs that are associated with any of the given list of sources in
     knowledge base.
    :vartype source_filter: list[str]
    :ivar logical_operation: Logical operation used to join metadata filter with source filter.
    :vartype logical_operation: str
    """

    _attribute_map = {
        "metadata_filter": {"key": "metadataFilter", "type": "MetadataFilter"},
        "source_filter": {"key": "sourceFilter", "type": "[str]"},
        "logical_operation": {"key": "logicalOperation", "type": "str"},
    }

    def __init__(
        self,
        *,
        metadata_filter: Optional["_models.MetadataFilter"] = None,
        source_filter: Optional[List[str]] = None,
        logical_operation: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword metadata_filter: Find QnAs that are associated with the given list of metadata.
        :paramtype metadata_filter: ~azure.ai.language.questionanswering.models.MetadataFilter
        :keyword source_filter: Find QnAs that are associated with any of the given list of sources in
         knowledge base.
        :paramtype source_filter: list[str]
        :keyword logical_operation: Logical operation used to join metadata filter with source filter.
        :paramtype logical_operation: str
        """
        super().__init__(**kwargs)
        self.metadata_filter = metadata_filter
        self.source_filter = source_filter
        self.logical_operation = logical_operation


class ShortAnswerOptions(_serialization.Model):
    """To configure Answer span prediction feature.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar enable: Enable or disable Answer Span prediction. Required. Default value is True.
    :vartype enable: bool
    :ivar confidence_threshold: Minimum threshold score required to include an answer span, value
     ranges from 0 to 1.
    :vartype confidence_threshold: float
    :ivar top: Number of Top answers to be considered for span prediction from 1 to 10.
    :vartype top: int
    """

    _validation = {
        "enable": {"required": True, "constant": True},
        "confidence_threshold": {"maximum": 1, "minimum": 0},
        "top": {"maximum": 10, "minimum": 1},
    }

    _attribute_map = {
        "enable": {"key": "enable", "type": "bool"},
        "confidence_threshold": {"key": "confidenceScoreThreshold", "type": "float"},
        "top": {"key": "topAnswersWithSpan", "type": "int"},
    }

    enable = True

    def __init__(self, *, confidence_threshold: Optional[float] = None, top: Optional[int] = None, **kwargs):
        """
        :keyword confidence_threshold: Minimum threshold score required to include an answer span,
         value ranges from 0 to 1.
        :paramtype confidence_threshold: float
        :keyword top: Number of Top answers to be considered for span prediction from 1 to 10.
        :paramtype top: int
        """
        super().__init__(**kwargs)
        self.confidence_threshold = confidence_threshold
        self.top = top


class TextAnswer(_serialization.Model):
    """Represents answer result.

    :ivar answer: Answer.
    :vartype answer: str
    :ivar confidence: answer confidence score, value ranges from 0 to 1.
    :vartype confidence: float
    :ivar id: record ID.
    :vartype id: str
    :ivar short_answer: Answer span object with respect to user's question.
    :vartype short_answer: ~azure.ai.language.questionanswering.models.AnswerSpan
    :ivar offset: The sentence offset from the start of the document.
    :vartype offset: int
    :ivar length: The length of the sentence.
    :vartype length: int
    """

    _validation = {
        "confidence": {"maximum": 1, "minimum": 0},
    }

    _attribute_map = {
        "answer": {"key": "answer", "type": "str"},
        "confidence": {"key": "confidenceScore", "type": "float"},
        "id": {"key": "id", "type": "str"},
        "short_answer": {"key": "answerSpan", "type": "AnswerSpan"},
        "offset": {"key": "offset", "type": "int"},
        "length": {"key": "length", "type": "int"},
    }

    def __init__(
        self,
        *,
        answer: Optional[str] = None,
        confidence: Optional[float] = None,
        id: Optional[str] = None,  # pylint: disable=redefined-builtin
        short_answer: Optional["_models.AnswerSpan"] = None,
        offset: Optional[int] = None,
        length: Optional[int] = None,
        **kwargs
    ):
        """
        :keyword answer: Answer.
        :paramtype answer: str
        :keyword confidence: answer confidence score, value ranges from 0 to 1.
        :paramtype confidence: float
        :keyword id: record ID.
        :paramtype id: str
        :keyword short_answer: Answer span object with respect to user's question.
        :paramtype short_answer: ~azure.ai.language.questionanswering.models.AnswerSpan
        :keyword offset: The sentence offset from the start of the document.
        :paramtype offset: int
        :keyword length: The length of the sentence.
        :paramtype length: int
        """
        super().__init__(**kwargs)
        self.answer = answer
        self.confidence = confidence
        self.id = id
        self.short_answer = short_answer
        self.offset = offset
        self.length = length


class TextDocument(_serialization.Model):
    """Represent input text record to be queried.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Unique identifier for the text record. Required.
    :vartype id: str
    :ivar text: Text contents of the record. Required.
    :vartype text: str
    """

    _validation = {
        "id": {"required": True},
        "text": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "text": {"key": "text", "type": "str"},
    }

    def __init__(self, *, id: str, text: str, **kwargs):  # pylint: disable=redefined-builtin
        """
        :keyword id: Unique identifier for the text record. Required.
        :paramtype id: str
        :keyword text: Text contents of the record. Required.
        :paramtype text: str
        """
        super().__init__(**kwargs)
        self.id = id
        self.text = text
