class map:
    def __init__(self) -> None:
        # (t = Top, b = Bottom) to differentiate top side and bottom side
        # R = Rook, B = Bishop, H = knigHt, K = King, Q = Queen, P = Pawn
        board = [
            ['tR', 'tB', 'tH', 'tK', 'tQ', 'tH', 'tB', 'tR' ]
            ['tP', 'tP', 'tP', 'tP', 'tP', 'tP', 'tP', 'tP' ]
            ['__', '__', '__', '__', '__', '__', '__', '__' ]
            ['__', '__', '__', '__', '__', '__', '__', '__' ]
            ['__', '__', '__', '__', '__', '__', '__', '__' ]
            ['__', '__', '__', '__', '__', '__', '__', '__' ]   
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP' ]
            ['bR', 'bB', 'bH', 'bK', 'bQ', 'bH', 'bB', 'bR' ]
        ]