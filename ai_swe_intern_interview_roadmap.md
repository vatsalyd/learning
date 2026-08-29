# AI Software Engineering Intern — Interview Roadmap

> **Goal:** Crack Software Engineering / AI Engineering internships with a practical, interview-first roadmap.
>
> **Principle:** Learn fewer tools deeply. Pair every concept with implementation, debugging, and interview questions. Avoid framework collecting and tutorial hell.

---

## 0. The Target Profile

The target is **not** a generic ML candidate and not a pure SWE candidate.

You want to become:

**Strong SWE fundamentals + Python/backend competence + practical ML/LLM engineering + ability to ship/debug an AI system.**

### Bottom → Top

```text
                         ┌──────────────────────┐
                         │  AI SYSTEM DESIGN    │
                         │  RAG • Agents • Eval │
                         └──────────┬───────────┘
                                    │
                         ┌──────────▼───────────┐
                         │ LLM / GenAI ENGINEER │
                         │ APIs • RAG • Tools   │
                         └──────────┬───────────┘
                                    │
                         ┌──────────▼───────────┐
                         │   ML FUNDAMENTALS    │
                         │ Models • Metrics     │
                         └──────────┬───────────┘
                                    │
                    ┌───────────────▼────────────────┐
                    │ SOFTWARE ENGINEERING / BACKEND │
                    │ FastAPI • SQL • APIs • Docker  │
                    └───────────────┬────────────────┘
                                    │
                    ┌───────────────▼────────────────┐
                    │     CS CORE + PYTHON            │
                    │ OOP • OS • Networking • Git     │
                    └───────────────┬────────────────┘
                                    │
                    ┌───────────────▼────────────────┐
                    │       DSA / PROBLEM SOLVING     │
                    │ Arrays → Trees → Graphs → DP    │
                    └───────────────┬────────────────┘
                                    │
                         ┌──────────▼───────────┐
                         │     PROGRAMMING      │
                         │       PYTHON         │
                         └──────────────────────┘
```

---

# 1. Python

## Learn

### Core

- Variables and types
- Conditions and loops
- Functions and scope
- Lists, tuples, sets, dictionaries
- Slicing
- Comprehensions
- Unpacking
- `*args`, `**kwargs`
- Lambda
- `map`, `filter`, `sorted`
- Exceptions
- Modules and packages
- Virtual environments

### Python internals

- Mutable vs immutable
- References
- `is` vs `==`
- Hashability
- Shallow vs deep copy
- Iterator vs iterable
- Generators and `yield`
- Decorators
- Context managers
- `__init__`, `__str__`, `__repr__`
- Inheritance
- Composition
- `@classmethod`
- `@staticmethod`
- Properties

### Engineering

- Type hints
- Dataclasses
- Logging
- Environment variables
- JSON
- HTTP requests
- `pytest`

## Do NOT spend time on

- Obscure metaprogramming
- CPython internals
- Advanced decorator wizardry
- Python trivia
- Every standard-library module

## Exercises

1. Word-frequency counter
2. Log parser
3. CSV → JSON converter
4. LRU cache
5. Retry decorator
6. Custom iterator
7. Generator pipeline
8. Simple CLI
9. HTTP API client
10. Mini task queue

## Interview questions

- Why is a dictionary O(1) on average?
- List vs tuple?
- What happens when you pass a list to a function?
- Shallow vs deep copy?
- Iterator vs generator?
- Why use generators?
- What does a decorator do?
- What happens when an exception is raised?
- Thread vs process?
- What is the GIL?

### Completion bar

Be able to **explain the mechanism and write a small example without help**.

---

# 2. DSA

The objective is **pattern recognition**, not solving hundreds of random problems.

## Sequence

### 2.1 Arrays & Strings

Learn:

- Traversal
- Two pointers
- Sliding window
- Prefix sums
- Frequency maps
- Sorting
- Binary search

Target: **20–25 problems**

### 2.2 Hashing

Learn:

- Hash map
- Hash set
- Frequency counting
- Lookup optimization

Target: **10–15 problems**

### 2.3 Linked Lists

Learn:

- Reverse
- Fast/slow pointer
- Cycle detection
- Merge lists
- Middle node

Target: **10 problems**

### 2.4 Stack / Queue

Learn:

- Stack
- Queue
- Deque
- Monotonic stack
- BFS

Target: **10–15 problems**

### 2.5 Trees

Learn:

- DFS
- BFS
- Recursion
- BST
- Height/depth
- Diameter
- LCA
- Path problems

Target: **15–20 problems**

### 2.6 Heap

Learn:

- Min heap
- Max heap
- Top K
- Merge K sorted structures
- Priority queue

Target: **10 problems**

### 2.7 Graphs

Learn:

- Adjacency list
- DFS
- BFS
- Connected components
- Cycle detection
- Topological sort
- Shortest path
- Union-Find

Target: **15–20 problems**

### 2.8 Dynamic Programming

Only after the above.

Learn patterns:

- 1D DP
- Grid DP
- Subsequence DP
- Knapsack
- Partition
- State transitions

Target: **15–20 problems**

## DSA total target

**120–150 carefully selected problems.**

## DSA completion bar

For a new medium problem:

```text
Identify pattern      < 5 min
Plan                  < 5 min
Implement             15–25 min
Explain complexity    Clearly
```

---

# 3. CS Fundamentals

## OOP

Know:

- Class/object
- Inheritance
- Polymorphism
- Abstraction
- Encapsulation
- Composition
- Interfaces
- SOLID basics

### Design patterns to know

- Factory
- Strategy
- Observer
- Singleton
- Adapter

Focus on **when and why**, not memorizing UML diagrams.

### Exercise

Design a **parking lot system**.

---

# 4. SQL + Databases

This is mandatory for AI engineering.

## SQL to master

```sql
SELECT
WHERE
GROUP BY
HAVING
ORDER BY
LIMIT
JOIN
LEFT JOIN
INNER JOIN
CASE
SUBQUERY
CTE
WINDOW FUNCTIONS
```

## Database concepts

- Primary key
- Foreign key
- Indexes
- Normalization
- Transactions
- ACID
- Isolation basics
- Query optimization basics

## Exercises

Use tables such as:

```text
users
orders
products
transactions
```

Practice:

- Top users by spending
- Monthly revenue
- Retention
- Duplicate detection
- Rolling average
- Ranking
- Cohort queries

Target: **40–50 SQL problems**

---

# 5. HTTP + Networking

You do not need deep networking certification knowledge.

You do need to understand web applications.

```text
Client
  ↓
DNS
  ↓
TCP
  ↓
HTTP
  ↓
Server
  ↓
Database
```

## Learn

- HTTP methods
- HTTP status codes
- Headers
- Cookies
- Sessions
- JWT
- REST
- JSON
- HTTPS
- DNS
- TCP vs UDP
- Request/response
- Timeout
- Retry
- Latency
- Connection lifecycle

## Interview questions

- PUT vs PATCH?
- What happens when you type `google.com` into a browser?
- What is a JWT?
- Why shouldn't every request be retried blindly?

---

# 6. Git + Linux

## Git

Know practically:

```bash
git clone
git status
git add
git commit
git push
git pull
git fetch
git merge
git rebase
git stash
git reset
git revert
git cherry-pick
git branch
git log
git diff
```

Be able to:

```text
Create branch
→ Implement feature
→ Resolve conflict
→ Rebase
→ Open PR
```

## Linux

Know:

```bash
ls
cd
pwd
cp
mv
rm
grep
find
cat
less
head
tail
curl
wget
chmod
ps
kill
top
df
du
ssh
```

Understand:

- Processes
- Ports
- Environment variables
- File permissions
- Logs

---

# 7. Software Engineering

This is where you move beyond "AI tutorial candidate".

## Project structure

```text
app/
├── api/
├── services/
├── models/
├── repositories/
├── utils/
├── config/
└── tests/
```

## Learn

- Separation of concerns
- Dependency injection
- Configuration management
- Error handling
- Logging
- Testing
- Validation
- Clean interfaces

## Testing

Learn:

- Unit tests
- Integration tests
- Mocks
- Fixtures
- Test isolation

Primary tool: **pytest**

---

# 8. FastAPI

One of the highest-value backend tools for AI engineering.

## Learn exactly

- Application structure
- Routing
- Path parameters
- Query parameters
- Request bodies
- Pydantic
- Validation
- Response models
- Dependency injection
- Middleware
- Exception handling
- Authentication
- Async endpoints
- Background tasks
- OpenAPI
- WebSockets — basic understanding

## Build

```text
POST /users
GET  /users/{id}
POST /chat
POST /documents
GET  /health
```

Then:

```text
FastAPI
   ↓
Service
   ↓
Database
```

Then:

```text
FastAPI
   ↓
LLM
```

Then:

```text
FastAPI
   ↓
RAG
   ↓
Vector DB
   ↓
LLM
```

---

# 9. Docker

You are not trying to become a DevOps engineer.

## Learn

```text
Dockerfile
Image
Container
Volume
Network
Port mapping
Environment variables
Docker Compose
```

Understand:

```text
Code
 ↓
Dockerfile
 ↓
Image
 ↓
Container
```

## Exercises

### Exercise 1

Containerize:

```text
FastAPI
+
PostgreSQL
```

### Exercise 2

```text
FastAPI
+
PostgreSQL
+
Redis
```

### Exercise 3

```text
FastAPI
+
LLM
+
Vector DB
```

### Completion bar

You should be able to explain **every line in your Dockerfile** and debug common container/network/port errors.

---

# 10. Cloud — AWS

Do not learn AWS broadly.

## Learn only

```text
EC2
ECR
IAM
S3
CloudWatch
VPC basics
```

Understand:

```text
Docker Image
      ↓
ECR
      ↓
EC2
      ↓
Application
```

Also know:

- Security groups
- SSH
- Environment secrets
- Logs
- Basic cloud networking

Do not spend weeks learning dozens of AWS services.

---

# 11. Machine Learning Fundamentals

You do not need to become a research scientist.

You need to understand models, evaluation and failure modes.

## Supervised learning

Learn:

- Linear regression
- Logistic regression
- Decision trees
- Random forest
- Gradient boosting
- XGBoost
- kNN
- SVM — conceptual

## Core concepts

- Train / validation / test
- Overfitting
- Underfitting
- Bias / variance
- Regularization
- Feature engineering
- Data leakage
- Cross-validation

## Metrics

### Classification

- Accuracy
- Precision
- Recall
- F1
- ROC-AUC
- PR-AUC

### Regression

- MAE
- MSE
- RMSE
- R²

## Practical exercise

Given a dataset:

```text
Inspect
 ↓
Clean
 ↓
Split
 ↓
Baseline
 ↓
Train
 ↓
Evaluate
 ↓
Diagnose
 ↓
Improve
```

## Key interview question

> Validation score is 95%, but production performance is terrible. Why?

Be ready to discuss:

- Data leakage
- Distribution shift
- Label mismatch
- Sampling bias
- Overfitting
- Preprocessing differences
- Monitoring gaps

---

# 12. Deep Learning

Only learn the pieces most useful for AI engineering.

## Learn

- Tensors
- Forward pass
- Loss
- Backpropagation
- Gradient descent
- Optimizers
- Learning rate
- Batch size
- Epoch
- Dropout
- Normalization
- Embeddings

## Neural network intuition

```text
Input
 ↓
Linear
 ↓
Activation
 ↓
Linear
 ↓
Loss
 ↓
Backprop
```

Also know:

- CNN — basic intuition
- RNN — basic intuition
- Transformer — deep understanding

Do not spend months manually implementing dozens of architectures.

---

# 13. Transformers / LLMs

This is core AI-engineering interview knowledge.

## Mental model

```text
Tokenization
 ↓
Embeddings
 ↓
Positional information
 ↓
Self-attention
 ↓
Feed-forward
 ↓
Transformer blocks
 ↓
Output probabilities
```

## Must know

- Tokens
- Tokenization
- Embeddings
- Positional encoding
- Self-attention
- Multi-head attention
- Q / K / V
- Context window
- Transformer architecture
- Autoregressive generation
- Temperature
- Top-k
- Top-p
- Hallucination
- Inference

## Interview questions

- What happens when you send a prompt to an LLM?
- Explain attention.
- Why Q, K and V?
- What does temperature do?
- Why do LLMs hallucinate?
- What limits context length?
- Fine-tuning vs RAG?

---

# 14. LLM APIs

Learn **one provider deeply**.

Preferred starting point: an **OpenAI-compatible API**.

Know other providers conceptually, but do not learn all SDKs deeply.

## Learn

- Chat / response APIs
- System and user messages
- Streaming
- Structured outputs
- Function / tool calling
- Token usage
- Retries
- Timeouts
- Rate limits
- Error handling
- Batching
- Caching

## Build

```text
User
 ↓
FastAPI
 ↓
LLM API
 ↓
Structured JSON
 ↓
Database
```

---

# 15. Embeddings + Vector Search

## Learn

- Embeddings
- Cosine similarity
- Dot product
- Euclidean distance
- Chunking
- Metadata
- Vector search
- Approximate nearest neighbor (ANN) intuition

## Data flow

```text
Document
 ↓
Chunks
 ↓
Embedding model
 ↓
Vectors
 ↓
Vector DB
```

## Choose one vector database

Recommended for your roadmap:

**Qdrant or ChromaDB**

Do not simultaneously learn every vector DB.

Understand other products conceptually only.

---

# 16. RAG

This is one of the highest-return AI-engineering topics.

Do not stop at a simple "PDF chatbot".

## Architecture

```text
                INGESTION

Documents
   ↓
Parsing
   ↓
Chunking
   ↓
Embedding
   ↓
Vector DB

                RETRIEVAL

Query
 ↓
Embedding
 ↓
Search
 ↓
Top K chunks
 ↓
Reranking
 ↓
Context
 ↓
LLM
 ↓
Answer
```

## Learn

- Chunking strategies
- Chunk overlap
- Metadata filtering
- Semantic search
- Hybrid search
- Reranking
- Top-k
- Retrieval precision
- Context recall
- Grounding
- Citations
- Hallucination mitigation

## Build a measurable RAG system

Track:

```text
Retrieval quality
Answer quality
Latency
Cost
```

---

# 17. LangChain + LangGraph

## LangChain — learn only what matters

Learn:

- Prompts
- Model interface
- Structured output
- Embeddings
- Retrievers
- Tools
- Message history
- Basic composition / LCEL concepts

Then stop.

Do not memorize every abstraction.

## LangGraph — higher value for agentic systems

Learn:

```text
State
Nodes
Edges
Conditional edges
Loops
Checkpointing
Interrupts
Persistence
```

Mental model:

```text
        ┌───────────┐
        │   Agent   │
        └─────┬─────┘
              ↓
           Decide
          /      \
       tool       answer
        ↓
      result
        ↓
       Agent
```

You should be able to explain:

> Why use a graph instead of a simple chain?

---

# 18. Agents

Do not start with multi-agent hype.

First understand:

```text
LLM + tools + state + loop
```

## Learn

- Tool calling
- Function calling
- ReAct
- Planning
- Memory
- State
- Tool selection
- Retries
- Failure handling
- Human-in-the-loop
- Guardrails

Then learn multi-agent systems.

## Key interview question

> Why does this system need an agent?

Strong reasoning:

> The system needs dynamic tool selection and iterative decision-making; if the execution path is deterministic, a normal workflow is simpler and more reliable.

---

# 19. AI Evaluation

This is a high-value differentiator.

## RAG evaluation

- Retrieval precision
- Retrieval recall
- Context relevance
- Faithfulness
- Answer relevance

## LLM evaluation

- Correctness
- Hallucination
- Format adherence
- Safety
- Latency
- Cost

## Agent evaluation

- Task success
- Tool accuracy
- Trajectory quality
- Failure rate

## Build an evaluation dataset

```text
question
expected_answer
retrieved_context
actual_answer
score
```

Run your system against it automatically.

---

# 20. Production AI

Now combine everything.

## Core architecture

```text
User
 ↓
API Gateway
 ↓
FastAPI
 ↓
Auth
 ↓
Application
 ↓
Cache
 ↓
Retriever
 ↓
LLM
 ↓
Database
```

## Operational layer

```text
Logs
Metrics
Tracing
Evaluation
```

## Learn

- Caching
- Rate limiting
- Retries
- Exponential backoff
- Circuit breakers
- Timeouts
- Streaming
- Async
- Queues
- Observability
- Cost optimization
- Prompt/version management
- Model fallback

Kubernetes is useful later, but it is not the first bottleneck for most intern interviews.

---

# 21. Basic System Design

For internships, focus on small practical systems before senior-level distributed systems.

## Design 1 — Chat API

```text
Client
 ↓
API
 ↓
LLM
 ↓
DB
```

## Design 2 — RAG System

```text
Upload
 ↓
Processing
 ↓
Embedding
 ↓
Vector DB

Query
 ↓
Retrieval
 ↓
LLM
```

## Design 3 — Rate Limiter

Understand:

- Token bucket
- Sliding window
- Redis

## Design 4 — URL Shortener

Understand:

- API
- Database
- Cache
- ID generation

## Design 5 — Notification / Task System

```text
API
 ↓
Queue
 ↓
Worker
 ↓
DB
```

---

# 22. Exact Tool Stack

Do not learn 30 technologies.

| Area | Tool / Technology | Depth |
|---|---|---|
| Language | Python | **Deep** |
| DSA | Python | **Deep** |
| Backend | FastAPI | **Deep** |
| API | REST / JSON | **Deep** |
| Database | PostgreSQL | **Deep enough for intern interviews** |
| Cache | Redis | **Practical** |
| Git | Git + GitHub | **Deep** |
| Containers | Docker + Compose | **Deep** |
| Cloud | AWS | **Practical** |
| ML | scikit-learn + XGBoost | **Deep fundamentals** |
| DL | PyTorch | **Practical + fundamentals** |
| Embeddings | Sentence Transformers | **Practical** |
| Vector DB | Qdrant / ChromaDB | **Deep in one** |
| LLM | OpenAI-compatible API | **Deep in API usage** |
| LLM framework | LangChain | **Selective** |
| Agent framework | LangGraph | **Deep enough to build** |
| Testing | pytest | **Practical** |
| Observability | Logging + tracing concepts | **Practical** |
| OS | Linux / WSL | **Practical** |

---

# 23. What NOT to Learn Yet

Avoid spending your main interview-prep time on:

- Kubernetes deep dives
- Terraform
- CUDA programming
- TensorRT internals
- Distributed training
- Ray
- Spark
- Kafka internals
- Airflow
- Hadoop
- Kubernetes operators
- Fine-tuning every open model
- Ten vector databases
- Ten agent frameworks
- Every AWS service
- Every LangChain abstraction
- Advanced reinforcement learning
- Research-level mathematics

These are useful later, but not your current bottleneck.

---

# 24. Interview Question Sequence

Do not prepare topics in isolation. Prepare for the sequence an interviewer is likely to follow.

## Round 1 — Coding

Typical progression:

```text
Easy array problem
        ↓
Hash map
        ↓
Sliding window
        ↓
Tree / graph
        ↓
Medium problem
```

## Round 2 — Python

Expect:

- Why Python?
- List vs tuple?
- How does a dictionary work?
- What is a generator?
- Explain async Python.

## Round 3 — Project deep dive

Expect:

- Why RAG?
- Why not fine-tuning?
- How did you chunk documents?
- Why that chunk size?
- Which embedding model?
- Why?
- Why that vector DB?
- How did you evaluate retrieval?
- What were your failure cases?

## Round 4 — LLM

Expect:

- How does attention work?
- What is an embedding?
- Why do hallucinations occur?
- What does temperature do?
- What is the context window?
- How would you reduce hallucinations?

## Round 5 — Backend

Expect:

- How does your API work?
- How do you handle concurrent requests?
- What happens if the LLM provider times out?
- How do retries work?
- How would you rate-limit users?

## Round 6 — AI System Design

Example:

> Design a production RAG system for 1M documents.

The interviewer will progressively scale:

```text
1 user
 ↓
100 users
 ↓
10k users
 ↓
1M users
```

And probe:

- Latency
- Cost
- Caching
- Queues
- Scaling
- Database
- Retrieval
- Model choice
- Failure handling
- Observability

---

# 25. Project Requirements

You do not need ten AI projects.

You need **2 highly defensible projects**.

## Project 1 — Production RAG

Build:

```text
Documents
    ↓
Ingestion pipeline
    ↓
Chunking
    ↓
Embeddings
    ↓
Qdrant
    ↓
Retriever
    ↓
Reranker
    ↓
LLM
    ↓
Citations
```

Use:

```text
FastAPI
PostgreSQL
Docker
Redis
pytest
AWS
logging
Evaluation
```

You should know every component.

## Project 2 — Agentic AI System

Build:

```text
User
 ↓
Agent
 ↓
Planner
 ↓
Tools
 ├── Search
 ├── Database
 ├── Calculator
 └── External API
 ↓
Evaluator
 ↓
Final answer
```

Use:

**LangGraph**

Add:

- State
- Retries
- Tool failure handling
- Memory
- Structured outputs
- Evaluation
- Tracing

This project should become your primary interview playground.

---

# 26. The Practice Loop

For every technology:

```text
LEARN
  ↓
BUILD
  ↓
BREAK
  ↓
DEBUG
  ↓
EXPLAIN
  ↓
INTERVIEW
```

Avoid:

```text
Tutorial
 ↓
Tutorial
 ↓
Tutorial
 ↓
Certificate
 ↓
Another framework
```

---

# 27. The 5-Level Mastery Test

Every topic should pass these five levels.

### Level 1 — Definition

> What is Docker?

### Level 2 — Mechanism

> How does Docker actually work?

### Level 3 — Implementation

> Containerize this FastAPI application.

### Level 4 — Failure

> The container starts but the API cannot reach PostgreSQL. Debug it.

### Level 5 — Design

> Design a production deployment for 10,000 users.

**Do not move to the next technology just because you completed a tutorial.**

Move when you can survive Level 4.

---

# 28. Priority Tiers

## S-Tier — Must Master

1. Python
2. DSA
3. SQL
4. Git
5. REST / HTTP
6. FastAPI
7. Docker
8. ML fundamentals
9. LLM fundamentals
10. RAG
11. LLM APIs
12. Project deep-dive ability

## A-Tier — Highly Valuable

13. PostgreSQL
14. Redis
15. Embeddings
16. Vector DB
17. LangGraph
18. Agents / tool calling
19. Evaluation
20. AWS
21. Testing
22. Linux
23. Basic system design

## B-Tier — After Above

24. Kubernetes
25. Celery / queues
26. OpenTelemetry
27. Model serving
28. vLLM
29. Deeper Hugging Face
30. Advanced MLOps

---

# 29. Final Interview Bar

You are ready when you can do all of the following **without ChatGPT**:

```text
LeetCode Medium
        ↓
Python implementation
        ↓
SQL query
        ↓
REST API design
        ↓
Debug Docker
        ↓
Explain ML model
        ↓
Explain Transformer
        ↓
Design RAG
        ↓
Design Agent
        ↓
Discuss production failures
```

And when an interviewer points to **any line in your project** and asks:

> **"Why did you do this?"**

you can answer technically and defend the tradeoff.

---

# 30. Highest-ROI Adjustment

If you already have experience with:

- Python
- FastAPI
- Docker
- AWS
- ChromaDB
- LangChain / LangGraph
- Multi-agent systems

**Do not restart from zero.**

The biggest ROI is usually in strengthening:

- DSA
- Python internals
- SQL
- Networking
- Backend engineering
- Testing
- Debugging
- System design

while turning your existing AI experience into **two deeply defensible projects**.

That combination is much stronger than adding another LLM framework to your resume.

---

# Master Strategy

```text
FOUNDATION
Python → DSA → SQL → Git → Linux → HTTP

        ↓

SOFTWARE ENGINEERING
OOP → Testing → FastAPI → PostgreSQL → Docker

        ↓

AI FOUNDATION
ML → PyTorch → Embeddings → Transformers

        ↓

GENAI ENGINEERING
LLM APIs → Structured Outputs → Tool Calling → RAG

        ↓

AGENTIC AI
LangGraph → State → Tools → Memory → Evaluation

        ↓

PRODUCTION
Redis → AWS → Observability → Reliability → Cost

        ↓

INTERVIEW
Coding → Project Deep Dive → AI Fundamentals → Backend → System Design
```

## The single rule to remember

> **Do not optimize for the number of technologies you know. Optimize for the number of systems you can build, break, debug, explain, and defend.**
