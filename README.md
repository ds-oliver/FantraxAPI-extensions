# FantraxAPI Extensions

This package provides additional tools and extensions for the [FantraxAPI](https://github.com/tarunbod/FantraxAPI) package.

## Features

### Lineup Optimizer

Automatically optimizes your Fantrax lineup based on:
- Starting player status
- Game times
- Player performance
- Position eligibility

### Waiver Wire Tools

Automates waiver wire interactions:
- Search for available players
- Place waiver claims
- Manage bids
- Handle player drops

## Installation

```bash
pip install fantrax-extensions
```

## Usage

### Lineup Optimizer

```python
from fantrax_extensions.lineup_optimizer import LineupOptimizer

optimizer = LineupOptimizer(api)
optimizer.optimize_lineup()
```

### Waiver Wire

```python
from fantrax_extensions.waiver_wire import WaiverManager

waiver = WaiverManager(api)
waiver.place_claim(player_to_add, player_to_drop, bid_amount)
```

## Requirements

- Python 3.6+
- FantraxAPI

## License

MIT License
