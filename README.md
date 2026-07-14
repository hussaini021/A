You are a Principal Quantitative Trading System Architect, Financial Market Microstructure Expert, ICT & Smart Money Concepts Specialist, Volume Profile Expert, Market Structure Specialist, Python Senior Engineer and Institutional Trading System Designer.

Your mission is to build a completely independent Institutional Market Intelligence Platform.

This is NOT a trading bot.

This is NOT a simple indicator.

This is NOT a signal generator.

This system must think like an institutional analyst before producing any trading plan.

====================================================

PROJECT NAME

====================================================

MN Market Intelligence Engine

====================================================

GOAL

====================================================

The objective is to understand the market exactly as an institutional trader.

Never generate Buy or Sell using one indicator.

Every decision must come from multiple confirmations.

If confirmations disagree,
the system must output:

WAIT

or

NO TRADE.

Never force a trade.

Capital protection has higher priority than trade frequency.

====================================================

EXECUTION

====================================================

Python 3.14+

Run

python run.py

Dashboard

dashboard.html

Localhost

http://localhost:13000

Dark institutional UI

Responsive

Professional animations

Real-time updates

No lag

====================================================

MT5 CONNECTION

====================================================

Read Only

Never place orders

Never modify MetaTrader

Never modify broker

Never create account

Never inject DLL

Never patch terminal

Never change settings

Only read market data.

If MT5 closes

Automatically reconnect.

====================================================

SYSTEM PHILOSOPHY

====================================================

Every module is independent.

Modules never make trading decisions.

Modules only analyze.

Decision Layer is the only module allowed to produce:

BUY

SELL

WAIT

NO TRADE

====================================================

ANALYSIS PIPELINE

====================================================

Market Data

↓

Market Regime

↓

Market Structure

↓

Liquidity

↓

Volume Profile

↓

Smart Money

↓

Order Flow

↓

VWAP

↓

Volatility

↓

Session

↓

Pullback Prediction

↓

Target Prediction

↓

Probability Engine

↓

Trade Planner

↓

Decision Layer

====================================================

DECISION PRINCIPLE

====================================================

Never Buy because one condition exists.

Never Sell because one condition exists.

Every Buy requires agreement between independent engines.

Every Sell requires agreement between independent engines.

If disagreement exists

WAIT.

If uncertainty is high

NO TRADE.

====================================================

SYSTEM PRIORITIES

====================================================

Priority 1

Capital Protection

Priority 2

Avoid False Entries

Priority 3

High Probability Context

Priority 4

Accurate Entry

Priority 5

Risk Reward

Priority 6

Trade Management

====================================================

MARKET STATES

====================================================

The system must always classify the market into exactly one dominant state.

Possible states

Strong Bull Trend

Weak Bull Trend

Strong Bear Trend

Weak Bear Trend

Balanced Range

Expansion

Compression

Manipulation

Accumulation

Distribution

Reversal

Continuation

Pullback

Exhaustion

Transition

High Volatility

Low Volatility

Institutional Activity

News Driven

====================================================

MAIN DASHBOARD

====================================================

Left Panel

Market Engines

Center

TradingView Style Chart

Right

Trade Planner

Bottom

Decision Layer

====================================================

LEFT PANEL

====================================================

Market Regime

Current Trend

Structure

Liquidity

Volume Profile

Smart Money

Order Flow

VWAP

ATR

Volatility

Session

Institutional Activity

Probability

Confidence

====================================================

CENTER CHART

====================================================

Display

HH

HL

LH

LL

Swing High

Swing Low

BOS

CHoCH

Liquidity

Liquidity Sweep

Equal High

Equal Low

Order Blocks

Breaker Blocks

Mitigation Blocks

Bullish FVG

Bearish FVG

Inverse FVG

Premium

Discount

Equilibrium

VAH

VAL

VPOC

HVN

LVN

VWAP

Anchored VWAP

Expected Pullback Zone

Projected Target

Entry

SL

TP1

TP2

TP3

====================================================

RIGHT PANEL

====================================================

Current Bias

Bullish

Bearish

Neutral

Current Regime

Current Trend

Setup Grade

Confidence

Trade Direction

BUY

SELL

WAIT

NO TRADE

Aggressive Entry

Moderate Entry

Conservative Entry

SL

TP1

TP2

TP3

Expected Duration

Risk Reward

Reasons

====================================================

BOTTOM PANEL

====================================================

Decision Layer

Every decision must explain:

Why Buy

Why Sell

Why Wait

Why No Trade

Never hide reasoning.

====================================================

ABSOLUTE RULES

====================================================

Never generate Buy without structure confirmation.

Never generate Sell without structure confirmation.

Never Buy into strong resistance.

Never Sell into strong support.

Never Buy directly below Buy Side Liquidity.

Never Sell directly above Sell Side Liquidity.

Never Buy in premium unless continuation is confirmed.

Never Sell in discount unless continuation is confirmed.

Never Buy before high impact news.

Never Sell before high impact news.

Never trade inside unclear structure.

Never trade during conflicting confirmations.

====================================================

SCORING SYSTEM

====================================================

Every engine returns

0-100

Decision Layer combines scores.

Example

Regime

95

Structure

92

Liquidity

90

Volume Profile

88

Order Flow

91

VWAP

86

Volatility

93

Session

90

Only when weighted score exceeds configured threshold and mandatory confirmations agree may the system issue BUY or SELL; otherwise it must output WAIT or NO TRADE with explicit reasons.

====================================================
MARKET REGIME ENGINE
====================================================

The Regime Engine is the highest priority analysis engine.

No BUY or SELL decisions are allowed before the current market regime is classified.

Every incoming candle must update the regime.

The engine must classify the market into one primary regime and one secondary regime.

Example:

Primary Regime:
Strong Bull Trend

Secondary Regime:
Pullback

Confidence:
93%

====================================================
OBJECTIVE
====================================================

Determine what type of market currently exists.

Never use only one indicator.

Use confluence between:

Market Structure

Liquidity

ATR

Swing Size

Momentum

Volume

VWAP

Volume Profile

Sessions

Trend Persistence

Price Efficiency

====================================================
SUPPORTED REGIMES
====================================================

Strong Bull Trend

Weak Bull Trend

Strong Bear Trend

Weak Bear Trend

Balanced Range

Expansion

Compression

Accumulation

Distribution

Manipulation

Continuation

Pullback

Exhaustion

Transition

High Volatility

Low Volatility

News Driven

Institutional Activity

====================================================
STRONG BULL TREND
====================================================

Conditions

Higher High

Higher Low

Bullish BOS confirmed

No bearish CHoCH

Price above VWAP

Price above Developing POC

ATR increasing

Bullish Momentum

No nearby strong resistance

Buy Side not yet exhausted

Output

Bullish Trend

Confidence

95-100

Trade Bias

BUY ONLY

Never Sell against this regime.

====================================================
STRONG BEAR TREND
====================================================

Conditions

Lower High

Lower Low

Bearish BOS

No bullish CHoCH

Below VWAP

Below POC

ATR increasing

Bearish Momentum

Output

Bearish Trend

Confidence

95-100

Trade Bias

SELL ONLY

====================================================
RANGE
====================================================

Conditions

No HH

No LL

Alternating BOS

ATR low

Volume average

Price oscillates between VAH and VAL

HVN dominant

Output

Range

Trade Bias

WAIT

Only Mean Reversion setups allowed.

====================================================
COMPRESSION
====================================================

Conditions

ATR decreasing

Swing length shrinking

Candles becoming smaller

Volume decreasing

No strong BOS

Output

Compression

Trade Bias

WAIT

Prepare for Expansion.

====================================================
EXPANSION
====================================================

Conditions

ATR expanding

Large candles

Strong BOS

Momentum increasing

Volume increasing

Output

Expansion

Trade Bias

Trend Continuation

====================================================
PULLBACK
====================================================

Conditions

Main trend still valid

Counter-trend move

No opposite BOS

Pullback toward:

VWAP

FVG

Order Block

VAL

VPOC

Discount

Output

Pullback Active

Trade Bias

WAIT

Do not enter until pullback finishes.

====================================================
PULLBACK COMPLETION
====================================================

Pullback completes when

Reaction appears

Liquidity collected

Bullish rejection

Structure preserved

Volume returns

Momentum resumes

Only then

BUY becomes possible.

====================================================
REVERSAL
====================================================

Conditions

CHoCH

Liquidity Sweep

Momentum loss

Opposite BOS

VWAP rejection

Volume confirmation

Output

Possible Reversal

Trade Bias

WAIT

Require confirmation.

====================================================
ACCUMULATION
====================================================

Conditions

Low volatility

Repeated support

Large absorption

Flat VWAP

Strong buying interest

Output

Accumulation

Bias

Prepare Bullish

====================================================
DISTRIBUTION
====================================================

Conditions

Repeated resistance

Weak highs

Buying exhaustion

Absorption

Output

Distribution

Bias

Prepare Bearish

====================================================
MANIPULATION
====================================================

Conditions

Large wick

Liquidity Sweep

Fast reversal

No follow-through

Volume spike

Output

Manipulation

Trade Bias

WAIT

Never chase manipulation candles.

====================================================
EXHAUSTION
====================================================

Conditions

Trend slowing

ATR falling

Momentum falling

Divergence

Repeated rejection

Output

Trend Exhaustion

Trade Bias

Reduce confidence.

====================================================
TRANSITION
====================================================

Conditions

Conflicting structure

Mixed momentum

Mixed liquidity

No clear direction

Output

Transition

Trade Bias

NO TRADE

====================================================
NEWS DRIVEN
====================================================

Conditions

High impact news

Extreme volatility

Spread expansion

Output

News Driven

Trade Bias

WAIT

No new entries until stability returns.

====================================================
REGIME SCORE
====================================================

Every regime receives

Confidence

0-100

Strength

0-100

Persistence

0-100

Quality

0-100

====================================================
DECISION RULES
====================================================

If

Trend Strong

AND

Structure Bullish

AND

Liquidity Bullish

AND

Pullback Completed

BUY Allowed

------------------------------------

If

Trend Strong

AND

Pullback Active

WAIT

------------------------------------

If

Range

WAIT

------------------------------------

If

Manipulation

WAIT

------------------------------------

If

Transition

NO TRADE

------------------------------------

If

News Driven

WAIT

------------------------------------

If

Strong Bear Trend

Only SELL setups allowed.

====================================================
OUTPUT
====================================================

Primary Regime

Secondary Regime

Confidence

Strength

Trade Bias

BUY ONLY

SELL ONLY

WAIT

NO TRADE

Reason

Every regime decision must explain why.
====================================================
MARKET STRUCTURE ENGINE
====================================================

The Structure Engine is responsible for understanding
how price is evolving.

It never generates BUY or SELL directly.

Its purpose is to identify:

• Trend Structure
• Swing Quality
• Internal Structure
• External Structure
• Break of Structure
• Change of Character
• Trend Health

====================================================
OBJECTIVE
====================================================

Analyze every completed candle.

Update the complete market structure in real time.

Every structure change must be logged.

====================================================
MAIN COMPONENTS
====================================================

Higher High (HH)

Higher Low (HL)

Lower High (LH)

Lower Low (LL)

Swing High

Swing Low

Major Swing

Minor Swing

Internal BOS

External BOS

Internal CHoCH

External CHoCH

Strong High

Weak High

Strong Low

Weak Low

Trend Strength

Trend Quality

====================================================
SWING DETECTION
====================================================

Every swing must satisfy:

Minimum price movement

Minimum candle separation

ATR filter

Ignore insignificant market noise.

Only confirmed swings may update structure.

====================================================
HIGHER HIGH
====================================================

Conditions

Previous confirmed High is broken.

Break closes above previous High.

Break is supported by momentum.

Swing Low remains valid.

Output

HH Confirmed

Trend Strength increases.

====================================================
HIGHER LOW
====================================================

Conditions

After HH

Price retraces

New Low stays above previous HL

Buyer reaction confirmed.

Output

HL Confirmed

Bullish Structure preserved.

====================================================
LOWER LOW
====================================================

Conditions

Previous confirmed Low broken.

Close below Low.

Momentum confirms.

Output

LL Confirmed

Bearish Structure strengthened.

====================================================
LOWER HIGH
====================================================

Conditions

Retracement fails below previous LH.

Seller reaction confirmed.

Output

LH Confirmed

Bearish continuation possible.

====================================================
BULLISH STRUCTURE
====================================================

Minimum Requirements

HH

HL

HH

HL

No bearish CHoCH

No bearish BOS

Output

Bullish Structure

Confidence increases.

====================================================
BEARISH STRUCTURE
====================================================

LL

LH

LL

LH

No bullish CHoCH

No bullish BOS

Output

Bearish Structure

====================================================
BREAK OF STRUCTURE
====================================================

Bullish BOS

Conditions

Previous Swing High broken.

Close above level.

Momentum confirmed.

Volume acceptable.

Output

Bullish BOS

Structure Score increases.

----------------------------------------------------

Bearish BOS

Previous Swing Low broken.

Close below level.

Momentum confirmed.

Output

Bearish BOS

====================================================
CHOCH
====================================================

Bullish CHoCH

Conditions

Previous bearish sequence interrupted.

New HH created.

Momentum improves.

Output

Possible bullish reversal.

Do NOT Buy immediately.

Wait for confirmation.

----------------------------------------------------

Bearish CHoCH

Previous bullish sequence interrupted.

New LL created.

Momentum weakens.

Output

Possible bearish reversal.

Wait.

====================================================
STRONG HIGH
====================================================

Definition

High defended by aggressive sellers.

Multiple rejections.

Large wick.

High volume.

No close above.

Output

Strong High

Resistance Score increases.

====================================================
WEAK HIGH
====================================================

Definition

High likely to be attacked.

Little rejection.

Poor structure.

Weak momentum.

Output

Weak High

Buy Side Liquidity vulnerable.

====================================================
STRONG LOW
====================================================

Definition

Strong buying response.

Large rejection.

High volume.

No close below.

====================================================
WEAK LOW
====================================================

Definition

Low likely to fail.

Weak reaction.

Poor buying pressure.

Sell Side Liquidity vulnerable.

====================================================
TREND HEALTH
====================================================

Healthy Trend

HH/HL sequence intact.

Momentum stable.

Pullbacks shallow.

Healthy.

----------------------------------------------------

Weak Trend

Swing quality decreasing.

Momentum slowing.

Lower confidence.

----------------------------------------------------

Exhausted Trend

Repeated failures.

Large divergence.

Weak BOS.

High reversal risk.

====================================================
STRUCTURE SCORE
====================================================

Calculate

Trend Quality

Swing Quality

BOS Quality

CHoCH Quality

Momentum

ATR

Volume

Score

0 - 100

====================================================
STRUCTURE CONFIDENCE
====================================================

Very Strong

90-100

Strong

80-89

Neutral

65-79

Weak

Below 65

====================================================
BUY ELIGIBILITY
====================================================

Structure alone NEVER authorizes BUY.

Structure only reports:

Bullish

Bearish

Neutral

Transition

Decision Layer must verify:

Liquidity

Regime

Volume Profile

Order Flow

Risk

Before BUY.

====================================================
SELL ELIGIBILITY
====================================================

Structure alone NEVER authorizes SELL.

Decision Layer must combine
all engines.

====================================================
WAIT CONDITIONS
====================================================

Mixed HH and LL

Conflicting BOS

Repeated CHoCH

Unclear swings

Low confidence

Output

WAIT

====================================================
NO TRADE CONDITIONS
====================================================

Structure Confidence below threshold.

Transition active.

Swing quality poor.

No dominant trend.

Output

NO TRADE

====================================================
DASHBOARD OUTPUT
====================================================

Current Trend

Bullish / Bearish / Neutral

Current Structure

HH

HL

LH

LL

Last BOS

Last CHoCH

Strong High

Strong Low

Weak High

Weak Low

Trend Health

Structure Score

Structure Confidence

Current State

Healthy

Weak

Transition

Exhausted

====================================================
TRADINGVIEW OVERLAY
====================================================

Display

HH

HL

LH

LL

Swing High

Swing Low

Bullish BOS

Bearish BOS

Bullish CHoCH

Bearish CHoCH

Strong High

Strong Low

Weak High

Weak Low

Trend Labels

Structure Score

====================================================
FINAL OUTPUT
====================================================

Structure Bias

Bullish

Bearish

Neutral

Confidence

Score

Trend Health

Reasons

Never output BUY or SELL here.

Only provide market structure analysis.
====================================================
LIQUIDITY ENGINE
====================================================

The Liquidity Engine detects where liquidity is located,
which liquidity has been taken,
which liquidity remains,
and which liquidity is the most probable future target.

The engine NEVER assumes liquidity will always be taken.

Every prediction must be probability based.

====================================================
OBJECTIVE
====================================================

Identify institutional liquidity areas.

Estimate which liquidity pools are attractive.

Detect completed liquidity sweeps.

Estimate next probable liquidity target.

====================================================
MAIN COMPONENTS
====================================================

Buy Side Liquidity

Sell Side Liquidity

Equal High

Equal Low

Liquidity Sweep

Liquidity Grab

Liquidity Void

Resting Liquidity

Untouched Liquidity

Consumed Liquidity

Next Liquidity Target

Liquidity Strength

Liquidity Score

====================================================
BUY SIDE LIQUIDITY
====================================================

Definition

Cluster of stop losses above previous highs.

Usually located:

Above Swing High

Above Equal High

Above Weak High

Above Range High

Above Previous Day High

Output

Location

Strength

Distance

Probability

====================================================
SELL SIDE LIQUIDITY
====================================================

Definition

Cluster of stop losses below previous lows.

Usually located:

Below Swing Low

Below Equal Low

Below Weak Low

Below Previous Day Low

Output

Location

Strength

Distance

Probability

====================================================
EQUAL HIGH
====================================================

Conditions

Two or more highs at nearly same price.

Tolerance configurable.

Volume accepted.

Output

Equal High

Potential Buy Side Liquidity.

====================================================
EQUAL LOW
====================================================

Conditions

Two or more lows at nearly same level.

Output

Equal Low

Potential Sell Side Liquidity.

====================================================
LIQUIDITY SWEEP
====================================================

Definition

Price trades beyond a known liquidity level
and then quickly rejects back.

Bullish Sweep

Price moves below Sell Side Liquidity

Then closes back above.

Bearish Sweep

Price moves above Buy Side Liquidity

Then closes back below.

Output

Sweep Confirmed

Sweep Direction

Sweep Strength

====================================================
SWEEP VALIDATION
====================================================

A sweep is higher quality when:

Occurs near session open.

Occurs after trend.

Occurs with strong rejection.

Occurs with volume increase.

Occurs near important structure.

Occurs near Value Area edge.

Occurs near Order Block.

Assign quality score.

====================================================
FAILED SWEEP
====================================================

If price breaks liquidity
and continues strongly
without rejection

Output

Liquidity Consumed

Do NOT classify as sweep.

====================================================
LIQUIDITY GRAB
====================================================

Definition

Small temporary penetration
without full structural confirmation.

Lower confidence than Sweep.

====================================================
LIQUIDITY VOID
====================================================

Definition

Fast movement through low participation area.

Characteristics

Large candles.

Little overlap.

Low traded volume.

Output

Void Zone

Probability of revisit.

====================================================
UNTOUCHED LIQUIDITY
====================================================

Detect liquidity levels never revisited.

Higher priority.

====================================================
NEXT LIQUIDITY TARGET
====================================================

Estimate next probable target using:

Current Structure

Trend

Volume Profile

Market Regime

Distance

Recent Sweep

Output

Next Target

Probability

Reason

====================================================
BULLISH LIQUIDITY CONTEXT
====================================================

Preferred context

Bullish Structure

SSL Sweep completed

Reaction confirmed

Trend intact

Volume acceptable

Output

Bullish Liquidity Context

====================================================
BEARISH LIQUIDITY CONTEXT
====================================================

Preferred context

Bearish Structure

BSL Sweep completed

Reaction confirmed

Trend intact

Output

Bearish Liquidity Context

====================================================
WAIT CONDITIONS
====================================================

Liquidity not reached.

Sweep incomplete.

Conflicting liquidity.

Price between major liquidity pools.

Output

WAIT

====================================================
NO TRADE CONDITIONS
====================================================

Liquidity unclear.

Weak Structure.

Multiple conflicting sweeps.

Low confidence.

Output

NO TRADE

====================================================
LIQUIDITY SCORE
====================================================

Components

Liquidity Quality

Distance

Sweep Quality

Structure Alignment

Volume Alignment

Session Alignment

Trend Alignment

Final Score

0 - 100

====================================================
TRADINGVIEW DISPLAY
====================================================

Display

Buy Side Liquidity

Sell Side Liquidity

Equal High

Equal Low

Liquidity Sweep

Liquidity Grab

Liquidity Void

Next Target

Probability

====================================================
DASHBOARD DISPLAY
====================================================

Current Liquidity

Nearest Buy Side Liquidity

Nearest Sell Side Liquidity

Nearest Sweep

Liquidity Score

Sweep Quality

Next Target

Reasons

====================================================
IMPORTANT RULE
====================================================

Liquidity alone NEVER creates BUY or SELL.

Liquidity only provides context.

Decision Layer must combine:

Regime

Structure

Liquidity

Volume Profile

Order Flow

Risk

before any trade decision.

Never issue BUY or SELL from Liquidity Engine alone.
====================================================
SMART MONEY ENGINE
====================================================

The Smart Money Engine identifies institutional price
inefficiencies and execution zones.

Never generate BUY or SELL directly.

Only detect, rank and validate Smart Money concepts.

====================================================
OBJECTIVE
====================================================

Detect high quality institutional trading zones.

Rank every zone.

Estimate probability of reaction.

Determine whether the zone remains valid.

====================================================
MODULES
====================================================

Bullish Order Block

Bearish Order Block

Breaker Block

Mitigation Block

Fair Value Gap

Inverse Fair Value Gap

Balanced Price Range

Optimal Trade Entry

Premium

Discount

Equilibrium

====================================================
BULLISH ORDER BLOCK
====================================================

Definition

The last bearish candle before an impulsive bullish move
that creates a confirmed Bullish BOS.

Requirements

Bullish BOS confirmed.

Strong displacement.

Volume acceptable.

No immediate invalidation.

Zone remains untouched or lightly mitigated.

Output

Bullish Order Block

Quality

Freshness

Probability

====================================================
BEARISH ORDER BLOCK
====================================================

Definition

Last bullish candle before impulsive bearish BOS.

Requirements

Bearish BOS.

Strong displacement.

Volume acceptable.

Fresh zone.

Output

Bearish Order Block

====================================================
ORDER BLOCK VALIDATION
====================================================

Increase score when

Near liquidity.

Near VWAP.

Near VAL or VAH.

Near Volume Profile edge.

Near FVG.

Near Session Open.

Decrease score when

Multiple retests.

Deep penetration.

Weak impulse.

Broken structure.

====================================================
MITIGATION BLOCK
====================================================

Definition

Institution returns to previously created Order Block
to complete unfilled orders.

Conditions

Original impulse remains valid.

Structure unchanged.

Reaction appears.

Output

Mitigation Active

====================================================
BREAKER BLOCK
====================================================

Definition

A failed Order Block that becomes support or resistance.

Conditions

Original Order Block invalidated.

Structure changed.

Zone reclaimed.

Output

Breaker Block

====================================================
FAIR VALUE GAP
====================================================

Definition

Three candle imbalance.

Bullish

Low of Candle 3 above High of Candle 1.

Bearish

High of Candle 3 below Low of Candle 1.

====================================================
FVG QUALITY
====================================================

Rank using

Gap Size

Impulse Strength

Volume

Trend Alignment

Regime Alignment

Liquidity Alignment

Freshness

Reaction History

Output

Grade

A+

A

B

C

Ignore

====================================================
FVG FILL
====================================================

The engine must detect

Untouched

Partially Filled

Completely Filled

Invalid

====================================================
INVERSE FVG
====================================================

Detect reclaimed FVG.

Estimate reversal probability.

====================================================
BALANCED PRICE RANGE
====================================================

Detect overlapping opposing FVGs.

Estimate breakout probability.

====================================================
OPTIMAL TRADE ENTRY
====================================================

Calculate

62%

70.5%

79%

retracement zone.

Combine with

Order Block

Liquidity

VWAP

FVG

Structure

====================================================
PREMIUM
====================================================

Price above equilibrium.

Prefer SELL context only
if other confirmations agree.

====================================================
DISCOUNT
====================================================

Price below equilibrium.

Prefer BUY context only
if confirmations agree.

====================================================
EQUILIBRIUM
====================================================

Middle of current dealing range.

Avoid aggressive entries here.

====================================================
BUY CONTEXT
====================================================

BUY context becomes stronger when

Bullish Regime

Bullish Structure

Discount

Bullish Order Block

Bullish FVG

Sell Side Liquidity Sweep completed

Positive Momentum

VWAP Support

No major resistance ahead

====================================================
SELL CONTEXT
====================================================

SELL context becomes stronger when

Bearish Regime

Bearish Structure

Premium

Bearish Order Block

Bearish FVG

Buy Side Liquidity Sweep completed

Negative Momentum

VWAP Resistance

====================================================
WAIT CONDITIONS
====================================================

Order Block exists
but

No confirmation.

FVG exists
but

Structure weak.

Liquidity missing.

Output

WAIT

====================================================
NO TRADE
====================================================

Old Order Block.

Filled FVG.

Broken Structure.

Conflicting Smart Money signals.

====================================================
SMART MONEY SCORE
====================================================

Freshness

Impulse

Volume

Alignment

Reaction

Quality

Final Score

0-100

====================================================
TRADINGVIEW
====================================================

Display

Bullish Order Block

Bearish Order Block

Mitigation

Breaker

Bullish FVG

Bearish FVG

Inverse FVG

Balanced Price Range

OTE

Premium

Discount

Equilibrium

Zone Grades

====================================================
DASHBOARD
====================================================

Nearest Bullish Order Block

Nearest Bearish Order Block

Nearest FVG

Freshness

Quality

Reaction Probability

Smart Money Score

====================================================
IMPORTANT RULE
====================================================

Never Buy because an FVG exists.

Never Sell because an Order Block exists.

Smart Money concepts are confirmation tools.

Final decisions belong only to Decision Layer.
Zone #1

Bullish Order Block

Grade: A+

Freshness: 98%

Reaction Probability: 87%

----------------------------------

Zone #2

Bullish FVG

Grade: A

Freshness: 91%

Reaction Probability: 74%

----------------------------------

Zone #3

Mitigation Block

Grade: B

Reaction Probability: 61%
====================================================
VOLUME PROFILE ENGINE
====================================================

The Volume Profile Engine identifies where the market
has accepted value and where price is likely to react.

Never generate BUY or SELL directly.

Only provide high-quality market context.

====================================================
OBJECTIVE
====================================================

Identify institutional value areas.

Detect high-volume acceptance zones.

Detect low-volume rejection zones.

Estimate future reaction probability.

====================================================
MODULES
====================================================

VAH

VAL

VPOC

HVN

LVN

Virgin POC

Developing POC

Composite Profile

Session Profile

====================================================
VALUE AREA HIGH
====================================================

Definition

Upper boundary of value area.

High probability resistance.

Conditions

Price reaches VAH.

Volume decreases.

Momentum weakens.

Liquidity nearby.

Output

Possible rejection.

Increase SELL probability only if
other engines confirm.

====================================================
VALUE AREA LOW
====================================================

Definition

Lower boundary of value.

High probability support.

Conditions

Price reaches VAL.

Buying reaction appears.

Momentum stabilizes.

Output

Possible bullish reaction.

Increase BUY probability only if
other engines confirm.

====================================================
VPOC
====================================================

Definition

Highest traded volume price.

Acts like institutional magnet.

Functions

Support

Resistance

Target

Magnet

Reaction Zone

====================================================
HVN
====================================================

Definition

High Volume Node.

Acceptance Area.

Characteristics

Slow movement.

Market balance.

Lower breakout probability.

====================================================
LVN
====================================================

Definition

Low Volume Node.

Price rejection area.

Characteristics

Fast movement.

Poor auction.

High breakout probability.

====================================================
VIRGIN POC
====================================================

POC never revisited.

Higher probability attraction.

====================================================
DEVELOPING POC
====================================================

Track real-time POC migration.

If POC moves upward

Bullish acceptance.

If downward

Bearish acceptance.

====================================================
PROFILE ALIGNMENT
====================================================

Bullish Context

Above POC

Holding above Value Area

Developing POC rising

LVN breakout

VAL defended

----------------------------------------------------

Bearish Context

Below POC

Holding below Value Area

POC falling

VAH rejected

====================================================
PROFILE SCORE
====================================================

Calculate

Acceptance

Rejection

Migration

Trend Alignment

Liquidity Alignment

Structure Alignment

Final Score

0-100

====================================================
WAIT CONDITIONS
====================================================

Price inside HVN.

No directional auction.

Balanced market.

Output

WAIT

====================================================
NO TRADE
====================================================

Balanced auction.

Conflicting profile.

Low confidence.

====================================================
TRADINGVIEW DISPLAY
====================================================

Display

VAH

VAL

VPOC

HVN

LVN

Virgin POC

Developing POC

====================================================
DASHBOARD
====================================================

Current Value Area

Distance to VAH

Distance to VAL

Current POC

Current HVN

Current LVN

Profile Score

Reaction Probability

====================================================
IMPORTANT RULE
====================================================

Never BUY because price touches VAL.

Never SELL because price touches VAH.

Volume Profile is only context.

Decision Layer decides.
Regime
Bullish
95%

Structure
Bullish
92%

Liquidity
Bullish
88%

Volume Profile
Bullish
91%

Order Flow
Bullish
94%

Smart Money
Bullish
89%

VWAP
Bullish
96%

Session
Bullish
90%

Confluence Score

92%

Status

Institutional Quality Setup
Current Market Story

Primary Trend:
Bullish

Structure:
HH-HL sequence intact

Liquidity:
Sell Side Liquidity swept

Smart Money:
Fresh Bullish Order Block respected

Volume Profile:
Price accepted above VPOC

Order Flow:
Buying pressure increasing

Current Expectation:
High probability of bullish continuation after pullback.

Current Risk:
Nearest Buy Side Liquidity only 12 points above.

Recommendation:
Wait for pullback into Bullish FVG before considering BUY.
====================================================
ORDER FLOW ENGINE
====================================================

The Order Flow Engine measures buying and selling pressure.

It NEVER generates BUY or SELL directly.

It measures who currently controls the market.

Institutional Buyers

Institutional Sellers

Balanced Market

====================================================
OBJECTIVE
====================================================

Determine:

Who is winning?

Buyers

Sellers

Nobody

Estimate probability of continuation.

Estimate probability of exhaustion.

Estimate probability of reversal.

====================================================
MODULES
====================================================

Delta

CVD

Footprint

Absorption

Exhaustion

Volume Imbalance

Iceberg Detection

Momentum Shift

Buying Pressure

Selling Pressure

====================================================
DELTA
====================================================

Definition

Difference between aggressive buying
and aggressive selling.

Positive Delta

Buyers dominant.

Negative Delta

Sellers dominant.

Delta Strength

Weak

Normal

Strong

Extreme

====================================================
CVD
====================================================

Definition

Cumulative Volume Delta.

Shows long-term pressure.

Bullish Conditions

Higher High

Higher Delta

Positive slope

Bearish Conditions

Lower Low

Negative Delta

Negative slope

====================================================
ABSORPTION
====================================================

Definition

Aggressive orders absorbed
without significant movement.

Bullish Absorption

Heavy selling.

Price refuses to fall.

Strong buyers active.

Bearish Absorption

Heavy buying.

Price refuses to rise.

Strong sellers active.

====================================================
EXHAUSTION
====================================================

Definition

Aggressive orders decreasing.

Trend slowing.

Volume decreasing.

Momentum fading.

Output

Possible reversal.

====================================================
VOLUME IMBALANCE
====================================================

Detect

Large imbalance.

Medium imbalance.

Small imbalance.

Measure strength.

====================================================
ICEBERG DETECTION
====================================================

Estimate hidden institutional orders.

Conditions

Repeated execution.

Price refuses movement.

Large volume.

Small price change.

Output

Possible Iceberg Activity.

====================================================
BUYING PRESSURE
====================================================

Increase score when

Positive Delta

Positive CVD

Bullish Absorption

Strong Momentum

High Volume

Structure Bullish

Liquidity Bullish

====================================================
SELLING PRESSURE
====================================================

Increase score when

Negative Delta

Negative CVD

Bearish Absorption

Strong Momentum

High Volume

Structure Bearish

Liquidity Bearish

====================================================
ORDER FLOW SCORE
====================================================

Calculate

Delta Score

CVD Score

Absorption Score

Momentum Score

Volume Score

Final Score

0 - 100

====================================================
BUY CONTEXT
====================================================

Bullish Structure

Bullish Regime

Positive Delta

Positive CVD

Buying Pressure

No major resistance

Liquidity supports BUY

Output

Bullish Context

====================================================
SELL CONTEXT
====================================================

Bearish Structure

Bearish Regime

Negative Delta

Negative CVD

Selling Pressure

Liquidity supports SELL

Output

Bearish Context

====================================================
WAIT CONDITIONS
====================================================

Positive Delta

Negative Structure

Mixed Signals

Conflicting Order Flow

Output

WAIT

====================================================
NO TRADE
====================================================

Weak Volume

No Delta Advantage

No Momentum

Balanced Order Flow

Output

NO TRADE

====================================================
TRADINGVIEW
====================================================

Display

Buying Pressure

Selling Pressure

Delta

CVD

Absorption

Exhaustion

Order Flow Score

====================================================
DASHBOARD
====================================================

Current Delta

Current CVD

Buying Pressure

Selling Pressure

Absorption

Exhaustion

Momentum

Order Flow Score

====================================================
IMPORTANT RULE
====================================================

Order Flow NEVER authorizes BUY.

Order Flow NEVER authorizes SELL.

Decision Layer must combine

Structure

Liquidity

Regime

Smart Money

Volume Profile

Risk

before issuing any trade.
====================================================
PULLBACK PREDICTION ENGINE
====================================================

The Pullback Prediction Engine predicts
high-probability retracement zones.

It NEVER assumes price MUST retrace.

It estimates probability.

====================================================
MISSION
====================================================

Predict

Will Pullback happen?

Expected Pullback Zone

Expected Pullback Depth

Expected Duration

Expected Completion Area

Expected Continuation Probability

====================================================
INPUTS
====================================================

Market Regime

Market Structure

Liquidity

FVG

Order Blocks

VWAP

Volume Profile

ATR

Momentum

Session

Swing Size

Trend Strength

====================================================
PULLBACK CONDITIONS
====================================================

Pullback probability increases when

Trend remains healthy

Strong BOS completed

Large displacement candle

Price extended from VWAP

Price extended from POC

Nearest FVG untouched

Nearest Order Block untouched

ATR high

No opposite BOS

====================================================
NO PULLBACK CONDITIONS
====================================================

Momentum accelerating

Expansion Phase

Liquidity immediately ahead

News driven movement

Very high buying pressure

Very high selling pressure

====================================================
PULLBACK DEPTH
====================================================

Estimate

Very Shallow

Shallow

Normal

Deep

Very Deep

====================================================
EXPECTED TARGETS
====================================================

Estimate reaction probability for

Nearest Bullish FVG

Nearest Bearish FVG

Nearest Order Block

Nearest Breaker Block

Nearest Mitigation Block

VWAP

Anchored VWAP

VAL

VAH

VPOC

Premium

Discount

Equilibrium

====================================================
PULLBACK QUALITY
====================================================

Grade

A+

A

B

C

Ignore

====================================================
COMPLETION CONDITIONS
====================================================

Pullback completes only when

Reaction appears

Structure remains valid

Liquidity collected

Momentum returns

Volume confirms

VWAP respected

====================================================
FAILED PULLBACK
====================================================

If opposite BOS appears

Structure breaks

Trend invalidated

Output

Pullback Failed

Reversal Risk High

====================================================
PULLBACK SCORE
====================================================

Trend Quality

Structure Quality

Momentum

ATR

Liquidity

Volume Profile

VWAP

Session

Final Score

0-100

====================================================
BUY CONTEXT
====================================================

Main Trend Bullish

Bullish BOS

Healthy HH HL

Pullback into

Discount

Bullish FVG

Bullish Order Block

VAL

VWAP

Liquidity already swept

Momentum stabilizing

Output

Bullish Pullback Ready

====================================================
SELL CONTEXT
====================================================

Main Trend Bearish

Bearish BOS

Healthy LH LL

Pullback into

Premium

Bearish FVG

Bearish Order Block

VAH

VWAP

Liquidity swept

Momentum weakening

Output

Bearish Pullback Ready

====================================================
WAIT CONDITIONS
====================================================

Pullback not finished

Liquidity untouched

No reaction

No confirmation

Output

WAIT

====================================================
NO TRADE CONDITIONS
====================================================

Pullback against strong regime

Weak structure

Mixed confirmations

Output

NO TRADE

====================================================
PULLBACK FORECAST
====================================================

Display

Current Price

Expected Pullback Zone

Expected Completion Zone

Expected Reaction Zone

Estimated Candle Count

Estimated Time

Probability

Reasons

====================================================
DASHBOARD
====================================================

Current Pullback

YES

NO

Expected Zone

Depth

Probability

Completion

Reaction Quality

====================================================
TRADINGVIEW
====================================================

Highlight

Projected Pullback Zone

Reaction Area

Expected Completion

Expected Continuation

====================================================
IMPORTANT RULE
====================================================

Never BUY because pullback started.

Never SELL because pullback started.

Trade only after pullback completion
and confirmation from Decision Layer.
Current Price

4001

Scenario 1

Bullish Continuation

Probability

67%

Expected Pullback

3993

Expected Target

4028

Expected Duration

3 Hours

-----------------------

Scenario 2

Deep Pullback

Probability

21%

Target

3985

-----------------------

Scenario 3

Bearish Reversal

Probability

12%

Target

3968
====================================================
TRADE PLANNER ENGINE
====================================================

The Trade Planner Engine creates
a complete institutional trade plan.

It never guesses.

It only creates a trade plan when
Decision Layer authorizes it.

====================================================
MISSION
====================================================

Generate

Trade Direction

Entry Zone

Entry Price

Stop Loss

TP1

TP2

TP3

Risk Reward

Trade Duration

Probability

Reasons

====================================================
ENTRY TYPES
====================================================

Aggressive Entry

Moderate Entry

Conservative Entry

====================================================
AGGRESSIVE ENTRY
====================================================

Conditions

Trend Strong

Structure Strong

Liquidity Confirmed

FVG Fresh

Order Block Fresh

Momentum High

Volume High

Confidence above 92%

Output

Immediate Entry Allowed

====================================================
MODERATE ENTRY
====================================================

Conditions

Trend confirmed

Wait for pullback

Wait for reaction

Wait for confirmation candle

Output

Preferred Entry

====================================================
CONSERVATIVE ENTRY
====================================================

Conditions

Pullback completed

Liquidity swept

Reaction confirmed

Bullish BOS

Order Flow confirms

Volume confirms

Decision Layer confirms

Output

Lowest Risk Entry

====================================================
ENTRY VALIDATION
====================================================

Before entry verify

Trend

Regime

Structure

Liquidity

Smart Money

Volume Profile

VWAP

Order Flow

ATR

Risk Reward

If one critical confirmation fails

Reject Entry

====================================================
STOP LOSS
====================================================

Priority

Behind Liquidity Sweep

Behind Swing

Behind Order Block

Behind FVG

ATR Buffer

Never place SL inside noise.

Minimum ATR buffer required.

====================================================
STOP LOSS VALIDATION
====================================================

Reject Stop Loss if

Too close

Inside FVG

Inside Liquidity

Inside Range

Below minimum ATR

====================================================
TP1
====================================================

Nearest logical objective

Partial close

====================================================
TP2
====================================================

Next institutional target

====================================================
TP3
====================================================

Final projected target

====================================================
TARGET PRIORITY
====================================================

Nearest Liquidity

VPOC

VAH

VAL

LVN

HVN

Order Block

FVG

Projected Swing

====================================================
BREAK EVEN
====================================================

Move SL only when

TP1 reached

Structure preserved

Momentum remains

====================================================
TRAILING STOP
====================================================

Update only after

New BOS

New HL

New LH

New confirmed swing

====================================================
TRADE DURATION
====================================================

Estimate

Scalp

Intraday

Swing

Estimate

Expected candles

Expected time

====================================================
RISK REWARD
====================================================

Reject any trade below configured RR.

Preferred

1:2

1:3

1:4

Higher preferred.

====================================================
BUY PLAN
====================================================

Trade

BUY

Entry Zone

Price

SL

TP1

TP2

TP3

Expected Duration

Confidence

Reasons

====================================================
SELL PLAN
====================================================

Trade

SELL

Entry Zone

Price

SL

TP1

TP2

TP3

Expected Duration

Confidence

Reasons

====================================================
WAIT PLAN
====================================================

WAIT

Reason

Missing confirmation

Missing liquidity

Pullback active

Weak volume

====================================================
NO TRADE PLAN
====================================================

NO TRADE

Reason

Conflicting structure

Weak trend

Poor RR

Low confidence

====================================================
TRADE SCORE
====================================================

Trend

Structure

Liquidity

Smart Money

Volume Profile

Order Flow

VWAP

Risk

RR

Confidence

Final Score

0-100

====================================================
DASHBOARD
====================================================

Trade Direction

BUY

SELL

WAIT

NO TRADE

Entry

SL

TP1

TP2

TP3

Risk Reward

Confidence

Reasons

====================================================
TRADINGVIEW
====================================================

Draw

Entry Line

SL Line

TP1

TP2

TP3

Projected Path

Projected Pullback

Projected Target

====================================================
IMPORTANT RULE
====================================================

Never create a trade plan unless
Decision Layer approves.

Every trade plan must explain WHY.
Trade Quality

Trend Quality

96%

Liquidity Quality

92%

Order Flow Quality

89%

Structure Quality

94%

FVG Quality

81%

Volume Profile

90%

VWAP

93%

Session

95%

Overall

91%

Grade

A+
====================================================
DECISION LAYER
====================================================

The Decision Layer is the brain of the system.

No Engine can generate BUY or SELL.

Only Decision Layer can generate

BUY

SELL

WAIT

NO TRADE

====================================================
MISSION
====================================================

Collect outputs from every Engine.

Evaluate them.

Assign weights.

Remove conflicting signals.

Generate only one final decision.

====================================================
INPUTS
====================================================

Market Regime

Market Structure

Liquidity

Smart Money

Volume Profile

Order Flow

VWAP

Session

ATR

Volatility

Risk

Pullback

Projected Target

====================================================
CRITICAL RULE
====================================================

Never generate BUY from one Engine.

Never generate SELL from one Engine.

Minimum confirmations required.

====================================================
WEIGHT SYSTEM
====================================================

Market Regime

20%

Market Structure

20%

Liquidity

15%

Smart Money

15%

Order Flow

10%

Volume Profile

8%

VWAP

5%

Session

3%

Volatility

2%

Risk

2%

====================================================
BUY CONDITIONS
====================================================

BUY is allowed ONLY if

Primary Regime

Bullish

AND

Structure

Bullish

AND

HH-HL intact

AND

Bullish BOS confirmed

AND

No Bearish CHoCH

AND

Liquidity

Sell Side Liquidity already swept

AND

Bullish Order Block

OR

Bullish FVG

AND

Price in Discount

OR

VWAP Support

AND

Positive Order Flow

AND

Positive Momentum

AND

Risk Reward acceptable

AND

No High Impact News

AND

Confidence above threshold

====================================================
BUY REJECTION
====================================================

Reject BUY if

Bearish CHoCH

Weak Structure

Price inside HVN

Price below VWAP

Strong Bearish Delta

Major resistance very close

RR below minimum

Multiple conflicts

Output

WAIT

====================================================
SELL CONDITIONS
====================================================

SELL only if

Primary Regime

Bearish

AND

LL-LH intact

AND

Bearish BOS

AND

No Bullish CHoCH

AND

Buy Side Liquidity swept

AND

Bearish Order Block

OR

Bearish FVG

AND

Price in Premium

OR

VWAP Resistance

AND

Negative Order Flow

AND

Momentum confirms

AND

Risk acceptable

====================================================
SELL REJECTION
====================================================

Reject SELL if

Bullish Structure

Bullish Delta

Strong Support

Discount

Weak Momentum

Conflicting Signals

====================================================
WAIT CONDITIONS
====================================================

WAIT if

Pullback active

Liquidity not reached

Order Block untouched

Mixed Structure

Mixed Order Flow

Mixed Volume

Mixed Regime

Unclear Trend

====================================================
NO TRADE CONDITIONS
====================================================

NO TRADE if

Structure Confidence

Below threshold

OR

Risk too high

OR

Spread abnormal

OR

ATR too low

OR

Market Transition

OR

News Driven

OR

Compression

OR

No Edge

====================================================
ENTRY VALIDATION
====================================================

Before Entry

Verify

Trend

Liquidity

FVG

Order Block

VWAP

Volume Profile

Order Flow

Risk

Session

Target

Only then

Allow Entry

====================================================
SL VALIDATION
====================================================

SL must be

Logical

Protected

Outside liquidity

Outside noise

ATR validated

====================================================
TP VALIDATION
====================================================

TP1

Nearest logical objective

TP2

Institutional objective

TP3

Projected liquidity

====================================================
TRADE CANCELLATION
====================================================

Cancel trade if

Opposite BOS

Opposite CHoCH

Liquidity Failure

News

Extreme volatility

Loss of Momentum

====================================================
CONFIDENCE
====================================================

Calculate

Trend

Structure

Liquidity

Smart Money

Order Flow

Volume Profile

VWAP

Risk

Final Confidence

0-100

====================================================
SETUP GRADE
====================================================

A+

95-100

A

90-94

B

80-89

C

70-79

Below 70

NO TRADE

====================================================
OUTPUT
====================================================

Direction

BUY

SELL

WAIT

NO TRADE

Entry

SL

TP1

TP2

TP3

Confidence

Grade

Reasons

Warnings

Alternative Scenario

====================================================
IMPORTANT
====================================================

Decision Layer must always explain

Why BUY

Why SELL

Why WAIT

Why NO TRADE

Never output a decision without explanation.

Every decision must be traceable.
Scenario A
Bullish Continuation
Probability 68%

Scenario B
Deep Pullback
Probability 21%

Scenario C
Bearish Reversal
Probability 11%
====================================================
RISK MANAGEMENT ENGINE
====================================================

The Risk Management Engine protects capital.

Capital protection always has higher priority than profit.

If risk is unacceptable,

No trade is allowed.

====================================================
MISSION
====================================================

Protect Capital

Reduce Drawdown

Filter Bad Trades

Manage Open Trades

Manage Stops

Manage Targets

Manage Risk

====================================================
RISK SCORE
====================================================

Calculate

Structure Risk

Liquidity Risk

Order Flow Risk

Volatility Risk

News Risk

Spread Risk

Session Risk

Trend Risk

Momentum Risk

Correlation Risk

Final Risk Score

0 - 100

====================================================
POSITION QUALITY
====================================================

Institutional

Excellent

Good

Average

Poor

Reject

====================================================
MAXIMUM RISK
====================================================

Reject any trade if

Risk Score > Allowed

Risk Reward below minimum

Stop Loss too wide

Spread too large

Market unstable

====================================================
STOP LOSS ENGINE
====================================================

Priority

1.

Behind Liquidity Sweep

2.

Behind Swing High / Swing Low

3.

Behind Order Block

4.

Behind FVG

5.

ATR Buffer

====================================================
INVALID STOP LOSS
====================================================

Reject Stop Loss if

Inside Liquidity

Inside FVG

Inside Order Block

Inside Noise

Too Close

Too Far

====================================================
BREAK EVEN ENGINE
====================================================

Move Stop Loss to Break Even only if

TP1 reached

Trend still healthy

Structure valid

Momentum unchanged

Order Flow still confirms

====================================================
TRAILING STOP
====================================================

Update Stop Loss after

New Higher Low

New Lower High

New BOS

New confirmed swing

Never trail randomly.

====================================================
TAKE PROFIT ENGINE
====================================================

TP1

Nearest logical objective

TP2

Next institutional objective

TP3

Major Liquidity

Projected Target

====================================================
PARTIAL CLOSE
====================================================

Allow

25%

50%

75%

Custom

====================================================
TRADE MANAGEMENT
====================================================

While trade is active

Continuously monitor

Trend

Liquidity

Order Flow

VWAP

Volume

Momentum

ATR

====================================================
TRADE EXIT CONDITIONS
====================================================

Exit immediately if

Strong opposite BOS

Strong opposite CHoCH

Institutional reversal

Major liquidity failure

Abnormal volatility

Emergency News

====================================================
POSITION SCORE
====================================================

Trend Quality

Entry Quality

Stop Quality

Target Quality

Liquidity Quality

Risk Quality

Final Position Score

====================================================
WARNING ENGINE
====================================================

Generate warnings

Weak Structure

High Volatility

News Ahead

Liquidity Nearby

Weak Momentum

Possible Reversal

Possible Pullback

====================================================
DASHBOARD
====================================================

Display

Risk Score

Trade Score

Position Score

Current Risk

Maximum Risk

Current Drawdown

Current RR

Trailing Stop

Break Even Status

====================================================
TRADINGVIEW
====================================================

Display

Entry

SL

Break Even

Trailing Stop

TP1

TP2

TP3

Risk Zone

Reward Zone

====================================================
FINAL OUTPUT
====================================================

Trade Approved

Trade Rejected

Reasons

Warnings

Recommendations

====================================================
IMPORTANT RULE
====================================================

Never increase risk after entry.

Never move Stop Loss further away.

Never revenge trade.

Never average into losing positions unless
a separately defined strategy explicitly allows it.
====================================================
MULTI-TIMEFRAME INTELLIGENCE ENGINE
====================================================

The Multi-Timeframe Intelligence Engine (MTIE)
is responsible for analyzing the market across
multiple timeframes before any trade is approved.

No BUY or SELL decision is allowed
without multi-timeframe confirmation.

====================================================
MISSION
====================================================

Determine

Primary Trend

Intermediate Trend

Execution Trend

Entry Timing

Trend Alignment

Structure Alignment

Liquidity Alignment

Momentum Alignment

====================================================
SUPPORTED TIMEFRAMES
====================================================

Monthly (MN)

Weekly (W1)

Daily (D1)

H4

H1

M30

M15

M5

M1

====================================================
TIMEFRAME ROLES
====================================================

MN

Macro Market Direction

W1

Institutional Bias

D1

Main Trend

H4

Swing Trend

H1

Intraday Bias

M30

Trade Preparation

M15

Execution Context

M5

Entry Timing

M1

Precision Entry

====================================================
TREND ALIGNMENT
====================================================

Each timeframe calculates

Trend

Structure

Liquidity

Momentum

VWAP

Volume Profile

Order Flow

ATR

Session

====================================================
PRIMARY TREND
====================================================

Use

Weekly

Daily

H4

Output

Primary Trend

Bullish

Bearish

Neutral

====================================================
EXECUTION TREND
====================================================

Use

M30

M15

M5

Output

Execution Direction

====================================================
FULL ALIGNMENT
====================================================

If

Weekly Bullish

Daily Bullish

H4 Bullish

H1 Bullish

M15 Bullish

Output

Institutional Bullish Alignment

Confidence increases.

====================================================
PARTIAL ALIGNMENT
====================================================

Example

Daily Bullish

H4 Bullish

H1 Pullback

M15 Pullback

M5 Reversal Trigger

Output

BUY Preparation

Not BUY Yet.

====================================================
CONFLICT DETECTION
====================================================

Example

Daily Bullish

H4 Bullish

M15 Bearish

Output

Counter Trend Pullback

Reduce confidence.

====================================================
MAJOR CONFLICT
====================================================

Example

Daily Bearish

H4 Bearish

H1 Bearish

M15 Bullish

Output

Counter Trend Rally

Reject aggressive BUY.

====================================================
MULTI TF STRUCTURE
====================================================

Detect

HH

HL

LH

LL

BOS

CHoCH

on every timeframe.

====================================================
MULTI TF LIQUIDITY
====================================================

Track

Weekly Liquidity

Daily Liquidity

Intraday Liquidity

Session Liquidity

====================================================
MULTI TF SMART MONEY
====================================================

Detect

Weekly Order Blocks

Daily Order Blocks

H4 Order Blocks

M15 Order Blocks

Prioritize higher timeframe zones.

====================================================
ZONE PRIORITY
====================================================

Priority

Weekly

Daily

H4

H1

M15

M5

====================================================
MULTI TF PULLBACK
====================================================

Detect

Higher timeframe pullback

Lower timeframe entry

Example

Daily Trend Bullish

H4 Pullback

M15 Bullish BOS

Output

High Probability BUY Context

====================================================
MULTI TF REVERSAL
====================================================

Detect

Weekly CHoCH

Daily BOS

H4 Reversal

M15 Trigger

Output

Institutional Reversal

====================================================
MULTI TF SCORE
====================================================

Weekly Score

Daily Score

H4 Score

H1 Score

M15 Score

M5 Score

Alignment Score

0-100

====================================================
CONFIDENCE
====================================================

95-100

Perfect Alignment

90-94

Strong Alignment

80-89

Acceptable

70-79

Weak

Below 70

Reject Trade

====================================================
BUY CONDITIONS
====================================================

BUY preferred when

Higher Timeframes Bullish

Execution Timeframe Bullish

Liquidity supports

Structure supports

Decision Layer approves

====================================================
SELL CONDITIONS
====================================================

SELL preferred when

Higher Timeframes Bearish

Execution Timeframe Bearish

Liquidity supports

Structure supports

Decision Layer approves

====================================================
WAIT CONDITIONS
====================================================

Higher timeframe bullish

Lower timeframe bearish

Wait until alignment.

====================================================
NO TRADE
====================================================

Strong conflict

Low confidence

Transition regime

====================================================
DASHBOARD
====================================================

Display

Weekly Bias

Daily Bias

H4 Bias

H1 Bias

M15 Bias

M5 Bias

Alignment

Confidence

Current Opportunity

====================================================
TRADINGVIEW
====================================================

Display

Trend Labels

Structure Labels

Liquidity Levels

Higher TF Zones

Current Entry TF

Alignment Status

====================================================
FINAL OUTPUT
====================================================

Primary Trend

Execution Trend

Alignment

Confidence

Trade Bias

Reasons

Warnings

====================================================
IMPORTANT RULE
====================================================

Never trade against the higher timeframe
unless a complete higher timeframe reversal
has been confirmed.

Higher timeframe always has priority
over lower timeframe.====================================================
MULTI-TIMEFRAME INTELLIGENCE ENGINE
====================================================

The Multi-Timeframe Intelligence Engine (MTIE)
is responsible for analyzing the market across
multiple timeframes before any trade is approved.

No BUY or SELL decision is allowed
without multi-timeframe confirmation.

====================================================
MISSION
====================================================

Determine

Primary Trend

Intermediate Trend

Execution Trend

Entry Timing

Trend Alignment

Structure Alignment

Liquidity Alignment

Momentum Alignment

====================================================
SUPPORTED TIMEFRAMES
====================================================

Monthly (MN)

Weekly (W1)

Daily (D1)

H4

H1

M30

M15

M5

M1

====================================================
TIMEFRAME ROLES
====================================================

MN

Macro Market Direction

W1

Institutional Bias

D1

Main Trend

H4

Swing Trend

H1

Intraday Bias

M30

Trade Preparation

M15

Execution Context

M5

Entry Timing

M1

Precision Entry

====================================================
TREND ALIGNMENT
====================================================

Each timeframe calculates

Trend

Structure

Liquidity

Momentum

VWAP

Volume Profile

Order Flow

ATR

Session

====================================================
PRIMARY TREND
====================================================

Use

Weekly

Daily

H4

Output

Primary Trend

Bullish

Bearish

Neutral

====================================================
EXECUTION TREND
====================================================

Use

M30

M15

M5

Output

Execution Direction

====================================================
FULL ALIGNMENT
====================================================

If

Weekly Bullish

Daily Bullish

H4 Bullish

H1 Bullish

M15 Bullish

Output

Institutional Bullish Alignment

Confidence increases.

====================================================
PARTIAL ALIGNMENT
====================================================

Example

Daily Bullish

H4 Bullish

H1 Pullback

M15 Pullback

M5 Reversal Trigger

Output

BUY Preparation

Not BUY Yet.

====================================================
CONFLICT DETECTION
====================================================

Example

Daily Bullish

H4 Bullish

M15 Bearish

Output

Counter Trend Pullback

Reduce confidence.

====================================================
MAJOR CONFLICT
====================================================

Example

Daily Bearish

H4 Bearish

H1 Bearish

M15 Bullish

Output

Counter Trend Rally

Reject aggressive BUY.

====================================================
MULTI TF STRUCTURE
====================================================

Detect

HH

HL

LH

LL

BOS

CHoCH

on every timeframe.

====================================================
MULTI TF LIQUIDITY
====================================================

Track

Weekly Liquidity

Daily Liquidity

Intraday Liquidity

Session Liquidity

====================================================
MULTI TF SMART MONEY
====================================================

Detect

Weekly Order Blocks

Daily Order Blocks

H4 Order Blocks

M15 Order Blocks

Prioritize higher timeframe zones.

====================================================
ZONE PRIORITY
====================================================

Priority

Weekly

Daily

H4

H1

M15

M5

====================================================
MULTI TF PULLBACK
====================================================

Detect

Higher timeframe pullback

Lower timeframe entry

Example

Daily Trend Bullish

H4 Pullback

M15 Bullish BOS

Output

High Probability BUY Context

====================================================
MULTI TF REVERSAL
====================================================

Detect

Weekly CHoCH

Daily BOS

H4 Reversal

M15 Trigger

Output

Institutional Reversal

====================================================
MULTI TF SCORE
====================================================

Weekly Score

Daily Score

H4 Score

H1 Score

M15 Score

M5 Score

Alignment Score

0-100

====================================================
CONFIDENCE
====================================================

95-100

Perfect Alignment

90-94

Strong Alignment

80-89

Acceptable

70-79

Weak

Below 70

Reject Trade

====================================================
BUY CONDITIONS
====================================================

BUY preferred when

Higher Timeframes Bullish

Execution Timeframe Bullish

Liquidity supports

Structure supports

Decision Layer approves

====================================================
SELL CONDITIONS
====================================================

SELL preferred when

Higher Timeframes Bearish

Execution Timeframe Bearish

Liquidity supports

Structure supports

Decision Layer approves

====================================================
WAIT CONDITIONS
====================================================

Higher timeframe bullish

Lower timeframe bearish

Wait until alignment.

====================================================
NO TRADE
====================================================

Strong conflict

Low confidence

Transition regime

====================================================
DASHBOARD
====================================================

Display

Weekly Bias

Daily Bias

H4 Bias

H1 Bias

M15 Bias

M5 Bias

Alignment

Confidence

Current Opportunity

====================================================
TRADINGVIEW
====================================================

Display

Trend Labels

Structure Labels

Liquidity Levels

Higher TF Zones

Current Entry TF

Alignment Status

====================================================
FINAL OUTPUT
====================================================

Primary Trend

Execution Trend

Alignment

Confidence

Trade Bias

Reasons

Warnings

====================================================
IMPORTANT RULE
====================================================

Never trade against the higher timeframe
unless a complete higher timeframe reversal
has been confirmed.

Higher timeframe always has priority
over lower timeframe.
Institutional Activity

Status:
High

Evidence:
✓ Large displacement
✓ Strong BOS
✓ Liquidity Sweep
✓ Volume Expansion
✓ Rising Developing POC

Estimated Institutional Participation:
High

Confidence:
89%
====================================================
MN MARKET INTELLIGENCE DASHBOARD
====================================================

The Dashboard must be designed as an
Institutional Trading Terminal.

Dark Theme

High Performance

Modern UI

Professional Animations

Real-Time Updates

No unnecessary graphics.

====================================================
LAYOUT
====================================================

----------------------------------------------------
TOP BAR
----------------------------------------------------

Current Symbol

Current Price

Spread

Session

Server Time

Market Status

Volatility

Market Regime

Institutional Activity

Connection Status

FPS

====================================================
LEFT PANEL
====================================================

MARKET ENGINES

Market Regime

Structure

Liquidity

Smart Money

Volume Profile

Order Flow

VWAP

ATR

Volatility

Risk

Decision Score

====================================================
CENTER
====================================================

TradingView Chart

Display

HH

HL

LH

LL

Swing High

Swing Low

Liquidity

Liquidity Sweep

Equal High

Equal Low

Order Blocks

Breaker Blocks

Mitigation Blocks

Bullish FVG

Bearish FVG

Premium

Discount

Equilibrium

VAH

VAL

POC

HVN

LVN

Projected Pullback

Projected Target

Entry

SL

TP1

TP2

TP3

====================================================
RIGHT PANEL
====================================================

TRADE PLANNER

Current Bias

BUY

SELL

WAIT

NO TRADE

Confidence

Setup Grade

Entry

Stop Loss

TP1

TP2

TP3

Risk Reward

Trade Duration

Reasons

Warnings

====================================================
BOTTOM LEFT
====================================================

STRUCTURE PANEL

Current Trend

HH Count

HL Count

LH Count

LL Count

Bullish BOS

Bearish BOS

Bullish CHoCH

Bearish CHoCH

Trend Health

Structure Quality

====================================================
BOTTOM CENTER
====================================================

LIQUIDITY PANEL

Nearest Buy Side Liquidity

Nearest Sell Side Liquidity

Nearest Sweep

Liquidity Score

Next Probable Target

Liquidity Quality

====================================================
BOTTOM RIGHT
====================================================

SMART MONEY PANEL

Nearest Order Block

Nearest FVG

Nearest Breaker

Nearest Mitigation

Premium

Discount

OTE

Zone Quality

====================================================
DECISION PANEL
====================================================

This panel must explain
every decision.

Example

Decision

BUY

Reason 1

Bullish Regime

Reason 2

Bullish Structure

Reason 3

Sell Side Liquidity Swept

Reason 4

Bullish FVG

Reason 5

Positive Order Flow

Reason 6

VWAP Support

Reason 7

RR 1:3

Confidence

94%

====================================================
ALTERNATIVE SCENARIOS
====================================================

Scenario A

Bullish Continuation

Probability

68%

----------------------------

Scenario B

Deep Pullback

Probability

22%

----------------------------

Scenario C

Bearish Reversal

Probability

10%

====================================================
WARNING PANEL
====================================================

High Impact News

Liquidity Nearby

Weak Momentum

High Volatility

Counter Trend

Low Confidence

Possible Reversal

====================================================
PULLBACK PANEL
====================================================

Pullback Active

YES

NO

Expected Zone

Expected Completion

Expected Duration

Expected Continuation

Probability

====================================================
MARKET STORY PANEL
====================================================

The dashboard must generate
human-readable explanations.

Example

"The higher timeframe trend remains bullish.

Price recently swept Sell Side Liquidity.

A fresh Bullish Order Block is holding.

Order Flow shows increasing buying pressure.

Price is currently retracing into Discount.

The preferred plan is to wait for confirmation before considering a BUY."

====================================================
TRADINGVIEW
====================================================

TradingView must synchronize

Entry

SL

TP1

TP2

TP3

Liquidity

Order Blocks

FVG

Projected Pullback

Projected Target

Decision

====================================================
REAL TIME UPDATE
====================================================

Update

Price

Every Tick

Market Structure

Every Candle Close

Liquidity

Every Tick

Order Flow

Every Tick

Decision Layer

Immediately after any important change

====================================================
IMPORTANT RULE
====================================================

Never repaint historical signals.

Never hide invalidated setups.

Mark cancelled setups clearly.

Keep all explanations transparent.
====================================================
FINAL SYSTEM INTEGRATION
====================================================

Project Name

MN Market Intelligence Engine

====================================================
MISSION
====================================================

Build a professional institutional market
analysis platform.

Never act like a simple indicator.

Think before every decision.

Every module must work independently.

Every module must send its output
to Decision Layer.

Decision Layer is the ONLY module
allowed to generate

BUY

SELL

WAIT

NO TRADE

====================================================
SYSTEM EXECUTION ORDER
====================================================

Step 1

Receive Market Data

↓

Step 2

Update Multi Timeframe Data

↓

Step 3

Update Sessions

↓

Step 4

Update ATR

↓

Step 5

Update Volatility

↓

Step 6

Market Regime Engine

↓

Step 7

Structure Engine

↓

Step 8

Liquidity Engine

↓

Step 9

Smart Money Engine

↓

Step 10

Volume Profile Engine

↓

Step 11

Order Flow Engine

↓

Step 12

Institutional Activity Engine

↓

Step 13

Pullback Prediction Engine

↓

Step 14

Target Projection Engine

↓

Step 15

Trade Planner Engine

↓

Step 16

Decision Layer

↓

Step 17

Dashboard Update

↓

Step 18

TradingView Update

====================================================
DATA FLOW
====================================================

Market Data

↓

Analysis Engines

↓

Scoring Engines

↓

Confluence Engine

↓

Decision Layer

↓

Trade Planner

↓

Dashboard

====================================================
CONFLUENCE ENGINE
====================================================

Before every decision calculate

Trend Alignment

Structure Alignment

Liquidity Alignment

Smart Money Alignment

Volume Alignment

Order Flow Alignment

VWAP Alignment

Session Alignment

Risk Alignment

Final Confluence Score

====================================================
CACHE
====================================================

Keep

Current Candle

Previous Candles

Current Structure

Current Liquidity

Current Sessions

Current Order Blocks

Current FVG

Current Decision

Automatically remove expired cache.

====================================================
THREADS
====================================================

Thread 1

Market Data

Thread 2

Analysis

Thread 3

Decision

Thread 4

Dashboard

Thread 5

Logging

Thread 6

TradingView

====================================================
ERROR HANDLING
====================================================

Never stop the system because
one engine fails.

Log error.

Restart failed engine.

Continue remaining engines.

====================================================
LOGGING
====================================================

Store

Timestamp

Engine

Decision

Reason

Confidence

Processing Time

Errors

====================================================
JSON OUTPUT
====================================================

Generate

Market Regime

Structure

Liquidity

Smart Money

Volume Profile

Order Flow

Institutional Activity

Pullback

Target

Trade Plan

Decision

Warnings

Confidence

====================================================
API
====================================================

Provide REST API

Provide WebSocket

Real Time Updates

====================================================
PERFORMANCE
====================================================

Low CPU Usage

Low RAM Usage

Fast Rendering

Fast Analysis

No Memory Leak

====================================================
SECURITY
====================================================

Read Only Access

Never modify MetaTrader

Never send orders

Never store passwords

Never expose API keys

====================================================
BACKTEST
====================================================

Allow replay.

Allow historical analysis.

Allow engine comparison.

Store results.

====================================================
SELF VALIDATION
====================================================

Before every decision verify

No missing data.

No conflicting calculations.

No invalid structure.

No invalid liquidity.

No invalid targets.

====================================================
AI REASONING
====================================================

Every decision must answer

Why?

Why not?

What changed?

What invalidates this trade?

What confirms this trade?

====================================================
SYSTEM HEALTH
====================================================

Monitor

CPU

RAM

Latency

Market Feed

Dashboard

TradingView

API

====================================================
FINAL OUTPUT
====================================================

Current Bias

Trade Direction

Confidence

Confluence Score

Setup Grade

Entry

Stop Loss

TP1

TP2

TP3

Warnings

Reasons

Alternative Scenario

====================================================
ABSOLUTE RULES
====================================================

Never force a trade.

Never guess.

Never hide uncertainty.

Always explain every decision.

Protect capital before profit.

Quality is more important than quantity.

Institutional logic always has priority.
