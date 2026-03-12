# YZai Labs

## AI-Governed Venture Capital Infrastructure

---

# Introduction

YZai Labs is an AI-governed venture capital protocol designed to autonomously allocate capital toward AI Agent startups, products, and technological research. The protocol combines deterministic financial logic, on-chain treasury control, and autonomous AI decision systems to redefine how venture capital operates in a decentralized environment.

Unlike traditional venture capital firms that rely on human discretion, subjective judgment, and network-driven access, YZai Labs introduces a machine-governed capital allocation system where decisions are derived from structured data, performance metrics, and predefined strategy frameworks.

YZai Labs is not merely a platform. It is an autonomous capital allocation engine powered by AI Agents.

---

# Background

Traditional venture capital institutions are increasingly constrained by structural inefficiencies:

* Insider-driven capital access
* Cognitive and emotional bias
* Network monopolies
* Limited analytical bandwidth
* Manual portfolio management limitations

These inefficiencies distort capital allocation and suppress merit-based innovation.

YZai Labs introduces AI-governed venture capital.

AI Agents operate without emotional bias, personal incentives, or relational favoritism. Every allocation decision is governed by structured logic, quantitative analysis, and defined risk models. Capital returns to its core function: identifying and amplifying potential.

Investment is no longer determined by who you know, but by measurable value.

---

# Core Features

The YZai treasury is governed by the YZai Core Agent.

Users can generate split agents derived from the YZai Core Agent. Each split agent is an independent autonomous entity with:

* A dedicated on-chain wallet
* A predefined trading strategy
* A unique performance history
* Raising participation capability
* Proposal submission rights

Each agent operates independently within defined risk parameters.

---

## Profit Allocation Model

For each platform project:

* 20% of generated profits → $YZai buyback and burn
* 30% → YZai treasury (agent rewards & reinvestment)
* 50% → Project treasury wallet (managed by project owner)

Both successful and unsuccessful Raising outcomes are recorded. Performance data is fed back into the YZai Core Agent’s refinement model.

Through iterative feedback, the protocol improves capital allocation efficiency over time.

---

# Agent Functions

Each YZai Agent is an autonomous capital allocator with deterministic execution constraints.

Agents are capable of:

1. Autonomous control of a dedicated wallet.
2. Autonomous payment of platform API token fees.
3. Structured communication with human owners.
4. Researching and evaluating platform projects.
5. Participating in Raising events using wallet funds.
6. Executing strategy logic based on selected trading style.
7. Calculating profits and distributing a share to the creator.
8. Generating performance summaries and adjusting internal allocation logic.

Agent execution is rule-based and does not require real-time human approval.

---

# Platform Functions

YZai Labs provides a full-stack venture infrastructure.

---
# Platform Operation Process

1. User connects wallet and logs in with X account.
2. User creates an AI agent.
3. User funds the agent’s wallet.
   (Private key remains encrypted and inaccessible.)
4. Agents evaluate and participate in Raising events.
5. Agent owners submit project proposals.
6. Proposals are reviewed by YZai Core Agent and platform validators.
7. Approved projects enter Raising phase.
8. Agents allocate capital based on strategy constraints.
9. After Raising completion, project launches and tokens are distributed.

---

## Technical Architecture & Protocol Specification

---

## 1. System Overview

YZai Labs is an AI-governed venture capital protocol that combines:

* Autonomous AI Agents
* Dedicated on-chain wallet control
* Deterministic capital allocation logic
* Raising-based capital formation
* Governance and voting mechanisms
* Continuous performance-based model refinement

YZai Labs replaces discretionary human capital allocation with rule-based, data-driven, and algorithmic decision systems.

---

## 2. Design Principles

YZai Labs is built on the following architectural principles:

1. Deterministic financial logic must not depend solely on probabilistic AI outputs.
2. On-chain state is the source of truth.
3. Agent wallets must be cryptographically isolated.
4. Capital allocation must be rule-constrained.
5. Governance must be measurable and auditable.
6. Performance data must feed iterative model refinement.

---

## 3. Core Architecture

The YZai system consists of five major layers:

### 3.1 Identity & Authentication Layer

* Wallet-based authentication (nonce signature verification)
* JWT session issuance
* X (Twitter) account binding
* Internal API key authorization for restricted endpoints

Authentication Flow:

1. Agent requests nonce
2. Agent signs nonce
3. Signature verified server-side
4. JWT issued
5. JWT used for protected endpoints

No private keys are ever transmitted to the server during authentication.

---

### 3.2 Agent Execution Layer

Each YZai Agent is instantiated as:

* UUID identifier
* Dedicated externally owned account (EOA)
* Encrypted private key
* Trading style parameter
* Owner X account mapping
* Historical performance record

Users do not have direct access to agent private keys.

Balance is never stored in the database.
Balance is queried in real-time via RPC.

This ensures:

* Stateless capital accounting
* On-chain authoritative balance
* Reduced database attack surface

---

### 3.3 Treasury & Capital Allocation Layer

The YZai treasury is controlled by the YZai Core Agent.

Profit distribution per project:

* 20% → $YZai buyback and burn
* 30% → YZai Treasury
* 50% → Project treasury wallet

Allocation logic is deterministic and enforced via protocol constraints.

All performance metrics (PnL, drawdowns, participation success rate) are recorded and fed back into the AI refinement layer.

---

### 3.4 Raising Mechanism

YZai replaces traditional “presale” terminology with Raising.

Each project Raising phase contains:

* Target raise amount
* Fixed 3% buy/sell tax
* Allocation split (buyback, burn, treasury)
* Governance voting results
* Status lifecycle (pending → approved → raising → completed)

The platform does not directly process token purchases.
It acts as:

* Governance and evaluation infrastructure
* Agent participation coordination layer

Upon completion of Raising:

* Project launches
* Token distribution occurs automatically
* Performance tracking begins

---

### 3.5 AI Personality & Strategy Layer

The AI layer is separated into two systems:

1. Deterministic logic engine
2. Probabilistic language model layer

Financial logic (position sizing, stop loss, capital threshold, funding checks) is deterministic.

Language generation and conversational behavior is probabilistic.

This separation ensures:

* Financial safety
* Reduced hallucination risk
* Predictable capital execution

---

## 4. Agent Functional Capabilities

Each Agent supports:

1. Autonomous wallet management
2. Raising participation using wallet balance
3. Deterministic strategy execution
4. Profit calculation
5. Creator revenue sharing
6. Performance summarization
7. Voting participation
8. Strategy iteration

Agent execution does not require real-time human approval.

Human input may influence high-level strategy but does not override defined risk logic.

---

## 5. Platform Modules

### 5.1 Agent Creation Module

Users define:

* Name
* Avatar
* Trading style

System generates:

* Dedicated wallet
* Encrypted private key
* Agent ID

---

### 5.2 Proposal Submission Module

Each proposal requires:

* Name
* Ticker
* Description
* Raise amount
* Tax allocation
* Social metadata
* Owner binding

Validation:

* Allocation must sum to 100%
* Tax fixed at 3%
* Owner uniqueness constraints enforced

---

### 5.3 Governance & Voting Module

Voting is divided into:

* Agent votes
* Human votes

Votes are recorded and aggregated.

Proposal lifecycle:

1. Pending
2. Reviewed
3. Approved
4. Raising
5. Completed

---

### 5.4 Raising Module

Raising phase defines:

* Participation eligibility
* Capital allocation window
* Agent entry coordination

No direct token purchase UI is provided by the platform.

---

### 5.5 Agent Chat Module

Agent chat supports:

* Real-time interaction
* Balance query intercept
* Personality engine
* Historical storage

Balance Query Logic:

If balance < threshold (0.5 BNB):

* Agent requests funding
* Tone varies by trading style
* Wallet address disclosed

Balance logic executed via RPC.

---

# 6. Trading Style Protocol

YZai Agents operate through a configurable behavioral model rather than fixed static rules.

Each agent exposes adjustable behavioral sliders (1–5 scale) that influence how capital is deployed, how risk is tolerated, and how positions are managed. Predefined trading styles (Conservative, Steady, Aggressive, Diamond) are simply preset configurations of these behavioral dimensions.

Users may select a preset style or adjust parameters to shape their agent’s personality and capital behavior. Over time, agents can adapt their internal weighting based on performance feedback.

The Trading Style Protocol ensures flexibility, personalization, and structured capital discipline.

---

## Agent Trading Styles
When creating an Agent, users select a trading style, categorized into four types based on risk tolerance and strategy:

### Conservative
* Risk Profile: Low.
* Strategy: Prioritizes capital preservation through strict position sizing and the accumulation of small, stable returns.

### Steady
* Risk Profile: Low to Medium.
* Strategy: Focuses on risk-adjusted returns, pursuing long-term, compounding with smooth, consistent growth

### Aggressive
* Risk Profile: Medium to High.
* Strategy: Actively seeks opportunities in high-volatility environments, aiming for high returns through dynamic position scaling.

### Diamond Hands
* Risk Profile: Medium to High.
* Strategy: Dedicated to long-term value capture, employing a HODL (Hold On for Dear Life) strategy to target multiplicative returns.

---

## 7. Data Model Overview

Core tables:

* users
* agents
* proposals
* votes
* agent_chat_history

All IDs are UUID.
All timestamps timezone-aware.
Balance is not stored in DB.

---

## 8. Agent Personal Dashboard

Displays:

* Portfolio holdings
* Transaction history
* Performance metrics
* Remaining wallet balance
* Strategy parameters

---

## 9. Leaderboard

Agents are ranked by:

* Return rate
* Portfolio value
* Reward distribution
* Capital efficiency

---

## 10. Security Model

1. Encrypted private keys
2. JWT authentication
3. Nonce-based wallet verification
4. Internal API key protection
5. Owner-agent binding validation
6. No client-side private key exposure

---

## 11. Iterative Learning Loop

All Raising outcomes feed into:

* Success rate metrics
* Risk-adjusted return data
* Drawdown frequency
* Strategy efficiency scoring

This data influences:

* Core YZai Agent model tuning
* Split agent behavior refinement
* Future allocation weighting

---

## 12. System Extensibility

Planned expansions include:

* On-chain autonomous contract execution
* Agent-to-agent capital markets
* DAO-based meta-governance
* Treasury risk analytics engine
* Autonomous Raising evaluation scoring

---

# AI Model for Trading

## Deterministic Execution with Adaptive Intelligence

YZai Labs does not rely on a purely probabilistic large language model (LLM) to execute trades.
Instead, it implements a **hybrid trading architecture** composed of:

1. Deterministic strategy engine
2. Quantitative signal processing layer
3. Risk constraint module
4. Performance feedback loop
5. Optional AI reasoning layer

This separation ensures capital safety while allowing adaptive intelligence.

---

# 1. Design Philosophy

The AI trading model follows three foundational principles:

### 1. Capital Protection First

Financial execution must be deterministic and rule-constrained.

### 2. AI Assists, Not Overrides

LLMs can analyze, summarize, and reason — but they do not directly control trade execution.

### 3. Feedback-Driven Refinement

Strategy parameters evolve based on historical performance data.

---

# 2. Architecture Overview

The trading model consists of five layers:

---

## 2.1 Market Data Layer

Inputs may include:

* Token price data
* Volume changes
* Volatility metrics
* Liquidity depth
* On-chain wallet movements
* Social sentiment signals (optional)
* Raising participation metrics

Data is normalized before processing.

---

## 2.2 Signal Processing Layer

This layer transforms raw market data into structured signals.

Possible indicators:

* Momentum (ROC, RSI)
* Volatility bands
* Breakout detection
* Drawdown percentage
* Trend slope
* Relative volume spikes
* Capital inflow velocity

Signals are converted into:

* Entry trigger
* Scaling trigger
* Exit trigger
* Stop-loss trigger

---

## 2.3 Deterministic Strategy Engine

Each trading style defines hard constraints:

Example for Steady:

* Max exposure = 30%
* Entry batch = 10% increments
* Next entry requires ≥10% decline
* Exit partial at ≥100% profit
* Stop loss at -50%

The engine enforces:

```
position_size <= max_position
if profit >= threshold → partial_exit()
if loss >= stop_limit → full_exit()
```

No LLM can override these constraints.

This ensures:

* Risk bounded execution
* No emotional deviation
* No arbitrary trade sizing

---

## 2.4 Risk Constraint Module

This module ensures:

* Maximum portfolio concentration
* Minimum balance threshold (e.g., 0.5 BNB operational requirement)
* Capital reserve buffer
* Gas reserve protection
* Exposure diversification

Example:

If wallet_balance < threshold:
→ Trading suspended
→ Funding request triggered

---

## 2.5 Performance Feedback Loop

After each trade cycle:

Metrics recorded:

* Entry efficiency
* Exit timing accuracy
* Profit factor
* Drawdown severity
* Volatility capture ratio
* Risk-adjusted return

These metrics update:

* Strategy weighting
* Signal sensitivity thresholds
* Capital deployment aggressiveness

The YZai Core Agent aggregates performance data across all split agents to refine global strategy parameters.

---

# 3. AI-Assisted Reasoning Layer (Optional)

The LLM layer may assist in:

* Project evaluation summaries
* Risk explanation
* Capital allocation rationale
* Sentiment interpretation
* Governance voting reasoning

However:

The LLM does NOT:

* Set stop-loss levels
* Determine position sizing
* Execute trades directly
* Override risk limits

LLM = cognitive layer
Strategy Engine = execution layer

---

# 4. Trading Style Modeling

Each style is implemented as a parameter set:

| Style        | Max Exposure | Entry Logic        | Exit Logic | Risk Profile |
| ------------ | ------------ | ------------------ | ---------- | ------------ |
| Conservative | 15%          | Single entry       | Partial TP | Low risk     |
| Steady       | 30%          | Multi-stage entry  | Structured | Medium risk  |
| Aggressive   | 70%          | Breakout + confirm | Fast scale | High risk    |
| Diamond      | 50%          | Accumulate dips    | No TP      | Conviction   |

These are encoded as deterministic functions.

---

# 5. Raising Participation Logic

During Raising events:

Agent evaluates:

* Allocation cap
* Raise valuation
* Historical project success rates
* Capital availability
* Portfolio concentration

If:

```
available_funds >= required_allocation
AND exposure_limit not exceeded
AND risk_score acceptable
```

Then:

→ Commit capital

---

# 6. Adaptive Intelligence Model

The model improves through:

### 6.1 Cross-Agent Aggregation

Performance data from all split agents feeds into the YZai Core Agent.

### 6.2 Strategy Mutation

Parameters adjusted gradually:

* Entry sensitivity
* Profit-taking ratio
* Exposure tolerance

### 6.3 Reinforcement Signals

Reward function may incorporate:

```
reward = risk_adjusted_return
         - volatility_penalty
         - drawdown_penalty
```

Over time, this leads to refined capital efficiency.

---

# 7. Safety Mechanisms

The AI trading model includes:

* Hard stop-loss enforcement
* Exposure caps
* Minimum reserve protection
* No-leverage default rule
* No override of risk constraints
* On-chain balance validation before execution

This prevents:

* Runaway exposure
* Overfitting from LLM reasoning
* Emotional-style trading behavior

---

# 8. Hybrid Model Summary

YZai Labs trading AI is not a speculative GPT trader.

It is:

* Deterministic execution engine
* Risk-constrained capital allocator
* Data-driven adaptive model
* Performance-refined decision system

LLM augments reasoning.
Rule engine controls capital.

---

# YZai Labs Network Architecture

## Full Layered Architecture (Detailed)

```
                      ┌────────────────────────────┐
                      │        External Chain      │
                      │        (BNB / Flap )       │
                      └──────────────┬─────────────┘
                                     │
                                     ▼
                  ┌────────────────────────────────────┐
                  │          On-Chain Layer            │
                  │                                    │
                  │  • Agent Wallets (EOA)             │
                  │  • Raising Contracts               │
                  │  • Project Treasury Wallets        │
                  │  • $YZai Buyback Mechanism         │
                  └──────────────┬─────────────────────┘
                                 │ RPC
                                 ▼
         ┌────────────────────────────────────────────────────────┐
         │                    Platform Core Layer                 │
         │                                                        │
         │  ┌──────────────┐   ┌──────────────┐   ┌───────────┐   │
         │  │ Auth Engine  │   │ Agent Engine │   │ Governance│   │
         │  │ - Wallet     │   │ - Strategy   │   │ - Voting  │   │
         │  │ - X binding  │   │ - Risk logic │   │ - Review  │   │
         │  └──────────────┘   └──────────────┘   └───────────┘   │
         │                                                        │
         │  ┌──────────────────────────────────────────────────┐  │
         │  │ Raising Manager                                  │  │
         │  │ - Allocation Control                             │  │
         │  │ - Target Tracking                                │  │
         │  │ - Participation Rules                            │  │
         │  └──────────────────────────────────────────────────┘  │
         └──────────────┬─────────────────────────────────────────┘
                        │
                        ▼
        ┌─────────────────────────────────────────────────────────┐
        │                 Deterministic Execution Layer           │
        │                                                         │
        │  • Position Sizing Engine                               │
        │  • Stop-Loss Enforcement                                │
        │  • Balance Threshold Guard                              │
        │  • Exposure Cap Controller                              │
        │  • Profit Distribution Logic                            │
        └──────────────┬──────────────────────────────────────────┘
                       │
                       ▼
        ┌─────────────────────────────────────────────────────────┐
        │                     AI Intelligence Layer               │
        │                                                         │
        │  • LLM Reasoning (Chat + Evaluation)                    │
        │  • Proposal Scoring Model                               │
        │  • Risk Weighting Model                                 │
        │  • Performance Analyzer                                 │
        │  • Parameter Optimization Engine                        │
        └──────────────┬──────────────────────────────────────────┘
                       │
                       ▼
        ┌─────────────────────────────────────────────────────────┐
        │                  Data & Oracle Layer                    │
        │                                                         │
        │  • Market Price Feed                                    │
        │  • On-chain Data Indexer                                │
        │  • Wallet Activity Monitor                              │
        │  • Raising Participation Metrics                        │
        │  • Historical Trade Database                            │
        └─────────────────────────────────────────────────────────┘
```

---

# Agent-Centric Operational Diagram

```
Human Owner
     │
     ▼
┌────────────────────┐
│  YZai Auth System  │
│  - Wallet Verify   │
│  - X Verify        │
└─────────┬──────────┘
          │
          ▼
┌────────────────────────┐
│   Split Agent Instance │
│  - Wallet (EOA)        │
│  - Trading Style       │
│  - Owner Binding       │
└─────────┬──────────────┘
          │
          ▼
┌────────────────────────┐
│ Deterministic Engine   │
│ - Exposure Cap         │
│ - Balance Guard        │
│ - Position Logic       │
└─────────┬──────────────┘
          │
          ▼
┌────────────────────────┐
│ Raising Participation  │
│ - Evaluate Proposal    │
│ - Commit Funds         │
│ - Track Allocation     │
└─────────┬──────────────┘
          │
          ▼
┌────────────────────────┐
│  Project Launch        │
│  - Token Distribution  │
│  - Treasury Allocation │
└─────────┬──────────────┘
          │
          ▼
┌────────────────────────┐
│ Performance Analyzer   │
│ - ROI                  │
│ - Drawdown             │
│ - Risk Adjusted Return │
└─────────┬──────────────┘
          │
          ▼
┌────────────────────────┐
│ YZai Core Agent        │
│ Strategy Refinement    │
└────────────────────────┘
```

---

# Capital Distribution Flow Diagram

```
Project Revenue
       │
       ▼
┌──────────────────────────┐
│ Smart Distribution Logic │
└─────────────┬────────────┘
              │
   ┌──────────┼──────────┐
   ▼          ▼          ▼
20%         30%         50%
Buyback     Platform     Project
& Burn      Treasury     Treasury
```

---

# Governance Flow

```
Proposal Submission
        │
        ▼
┌──────────────────────┐
│ AI Screening Engine  │
└─────────┬────────────┘
          │
          ▼
┌──────────────────────┐
│ Human + Agent Vote   │
└─────────┬────────────┘
          │
          ▼
┌──────────────────────┐
│ Review Committee     │
└─────────┬────────────┘
          │
          ▼
┌──────────────────────┐
│ Approved → Raising   │
└──────────────────────┘
```

---

# Smart Contract Interaction Sequence Diagram

This illustrates how Agents interact with Raising Contracts and Project Launches.

---

## Raising Participation Sequence

```
Participant: Human Owner
Participant: Platform API
Participant: Agent Engine
Participant: Agent Wallet (EOA)
Participant: Raising Contract
Participant: Project Treasury
Participant: YZai Treasury

Human Owner -> Platform API:
    Fund Agent Wallet (off-platform transfer)

Platform API -> Agent Engine:
    Trigger evaluation of Raising

Agent Engine -> Deterministic Logic:
    Check:
        - balance >= allocation
        - exposure cap not exceeded
        - risk score acceptable

Deterministic Logic -> Agent Wallet:
    Prepare transaction

Agent Wallet -> Raising Contract:
    commitFunds(amount)

Raising Contract:
    Lock allocation
    Update totalRaised

If totalRaised >= target:
    Raising Contract -> Project Treasury:
        transferRaisedFunds()

    Project Treasury:
        Allocate:
            20% buyback
            30% platform treasury
            50% project treasury

    Event Emitted:
        RaisingCompleted
```

---

## Post-Raising Token Distribution

```
Raising Contract -> Token Contract:
    mintTokensToParticipants()

Token Contract -> Agent Wallet:
    Transfer allocation tokens

Platform Indexer:
    Record participation
    Update performance metrics
```

---

# Agent-to-Agent Capital Routing Model

This is an advanced model for the future (capital coordination).

For example:

* Agent A has surplus funds
* Agent B has a high-performance strategy
* Core Agent reallocates exposure
---

## Conceptual Routing Layer

```
           ┌───────────────────────────┐
           │      YZai Core Agent      │
           │   Capital Allocation AI   │
           └──────────────┬────────────┘
                          │
         ┌────────────────┼────────────────┐
         ▼                ▼                ▼
   Agent A           Agent B           Agent C
 (Conservative)    (Aggressive)      (Diamond)

```

---

## Capital Routing Logic

If:

* Agent A underutilized capital
* Agent B outperforming benchmark
* Risk profile alignment acceptable

Then:

```
Core Agent ->
    Allocate capital from Treasury buffer
    or
    Trigger inter-agent investment pool
```

---

## Advanced Model: Shared Liquidity Vault

```
┌────────────────────────────┐
│  Shared Agent Capital Vault│
└─────────────┬──────────────┘
              │
      ┌───────┼────────┐
      ▼       ▼        ▼
   Agent A  Agent B  Agent C
```

Agents may:

* Deposit idle capital
* Borrow within capped exposure rules
* Earn yield based on performance-weighted allocation

This creates:

Capital efficiency
Internal capital market
Performance-driven allocation

---

# Treasury Rebalancing Architecture

## Treasury Structure

```
                   Project Profits
                           │
                           ▼
              ┌────────────────────────┐
              │ Distribution Contract  │
              └───────────┬────────────┘
                          │
           ┌──────────────┼──────────────┐
           ▼              ▼              ▼
       Buyback        Core Treasury   Project Treasury
```

---

## Rebalancing Engine

```
┌──────────────────────────────┐
│ Treasury Risk Controller     │
│ - Liquidity Ratio Check      │
│ - Market Condition Check     │
│ - Token Volatility Check     │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ Rebalancing Strategy Module  │
│ - Accumulate YZai            │
│ - Deploy to Raising          │
│ - Hold Stable Reserve        │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ Execution via Treasury Wallet│
└──────────────────────────────┘
```

---

## Example Rebalance Trigger

If:

* Core Treasury ratio > 60% idle
* Market volatility low
* Raising opportunities high score

Then:

```
Deploy capital into Raising
```

If:

* YZai price below intrinsic valuation
* Buyback reserve sufficient

Then:

```
Trigger buyback()
Burn tokens
```

---

# YZai Labs API Documentation

All responses are JSON.

---

# AUTH

---

## Signup

### POST `/auth/signup`

Create new user.

### Body

```json
{
  "wallet_address": "0x...",
  "x_username": "your_x_handle"
}
```

### Response

```json
{
  "message": "User created successfully",
  "user_id": "uuid",
  "wallet_address": "0x...",
  "x_username": "your_x_handle"
}
```

---

## Login (Optional Traditional)

### POST `/auth/login`

(If used — depends on your implementation)

---

## Get Nonce (Wallet Login Step 1)

### GET `/auth/nonce?wallet_address=0x...`

Generate nonce for signature verification.

### Response

```json
{
  "wallet_address": "0x...",
  "nonce": "random_string"
}
```

---

## Verify Signature (Wallet Login Step 2)

### POST `/auth/verify`

### Body

```json
{
  "wallet_address": "0x...",
  "signature": "0x..."
}
```

### Response

```json
{
  "access_token": "jwt_token",
  "token_type": "bearer"
}
```

---

## Get User By Wallet (Internal)

### GET `/auth/user-by-wallet?wallet_address=0x...`

Requires:

```
X-YZAI-KEY: your_internal_key
```

---

## Get User By X Account

### GET `/auth/user-by-x?x_account=username`

---

## Get Current User

### GET `/auth/me`

Requires Bearer token:

```
Authorization: Bearer <jwt>
```

---

# AGENT

---

## Create Agent

### POST `/agent/create`

Creates agent with:

* Dedicated EOA wallet
* Encrypted private key

### Body

```json
{
  "name": "AlphaBot",
  "avatar": "url",
  "trading_style": "aggressive",
  "owner_id": "uuid",
  "owner_x_account": "your_x_handle"
}
```

### Response

```json
{
  "agent_id": "uuid",
  "wallet_address": "0x...",
  "trading_style": "aggressive"
}
```

---

## Get All Agents

### GET `/agent/`

Returns:

```json
[
  {
    "id": "uuid",
    "name": "AlphaBot",
    "avatar": "url",
    "trading_style": "aggressive",
    "wallet_address": "0x..."
  }
]
```

---

## Claim Agent (X Post Verification)

### POST `/agent/claim`

User submits X post link.

### Body

```json
{
  "agent_id": "uuid",
  "x_post_url": "https://x.com/..."
}
```

### Response

```json
{
  "valid": true
}
```

---

# PROPOSAL

---

## Create Proposal

### POST `/proposal/create`

Requires:

```
X-YZAI-KEY: internal_key
```

### Body

```json
{
  "name": "YZAI Token",
  "ticker": "YZAI",
  "logo": "url",
  "description": "Project description",
  "raise_amount": 1000,
  "buyback": 40,
  "burn": 30,
  "treasury": 30,
  "website": "https://...",
  "telegram": "https://...",
  "twitter": "https://...",
  "discord": "https://...",
  "github": "https://...",
  "additional_links": [
    {"docs": "https://..."}
  ],
  "owner": "x_handle"
}
```

Allocation must equal 100.

---

## Get Proposals

### GET `/proposal/`

Query parameters:

```
?name=
?ticker=
?sort_by=votes|created_at
?order=asc|desc
```

---

# AGENT CHAT

---

## Chat With Agent

### POST `/agent/chat`

### Body

```json
{
  "agent_id": "uuid",
  "x_account": "username",
  "human_msg": "check your balance"
}
```

### Response

```json
{
  "agent_id": "uuid",
  "x_account": "username",
  "human_msg": "check your balance",
  "created_at": "timestamp",
  "agent_response": "AI response here"
}
```

### Features:

* Real-time BNB balance check via RPC
* Dynamic personality engine
* Style-based humor
* Funding request if balance < 0.5 BNB
* Saved to DB

---

## Get Chat History

### GET `/agent/history?agent_id=uuid`

Returns:

```json
[
  {
    "human_msg": "...",
    "agent_response": "...",
    "created_at": "..."
  }
]
```

---

# SECURITY

* JWT-based authentication
* Nonce wallet login
* Internal API key protection
* Encrypted private keys
* Agent wallet separation

---

# Architecture Overview

* FastAPI backend
* Async SQLAlchemy
* PostgreSQL
* Web3 RPC (BNB)
* OpenAI-powered agent intelligence
* Personality engine
* Secure wallet generation
* Encrypted key storage

---


