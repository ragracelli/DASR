import math

import torch
import torch.nn as nn
import torch.nn.functional as F
import separableconv.nn as scnn

class PositionalEncoding(nn.Module):
    """Implement the positional encoding (PE) function.

    PE(pos, 2i)   = sin(pos/(10000^(2i/dmodel)))
    PE(pos, 2i+1) = cos(pos/(10000^(2i/dmodel)))
    """

    def __init__(self, d_model, max_len=5000):
        super(PositionalEncoding, self).__init__()
        # Compute the positional encodings once in log space.
        pe = torch.zeros(max_len, d_model, requires_grad=False)
        position = torch.arange(0, max_len).unsqueeze(1).float()
        div_term = torch.exp(torch.arange(0, d_model, 2).float() *
                             -(math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0)
        self.register_buffer('pe', pe)

    def forward(self, input):
        """
        Args:
            input: N x T x D
        """
        length = input.size(1)
        return self.pe[:, :length]

'''
class DepthwiseSeparableConv(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size):
        super(DepthwiseSeparableConv, self).__init__()
        self.depthwise = nn.Conv1d(in_channels, in_channels, kernel_size=kernel_size, groups=in_channels)
        self.pointwise = nn.Conv1d(in_channels, out_channels, kernel_size=1)

    def forward(self, x):
        x = self.depthwise(x.unsqueeze(2))
        x = self.pointwise(x.unsqueeze(2))
        return x.squeeze(2)
'''
class PositionwiseFeedForward(nn.Module):
    """Implements position-wise feedforward sublayer.

    FFN(x) = max(0, xW1 + b1)W2 + b2
    """

    def __init__(self, d_model, d_ff, dropout=0.1):
        super(PositionwiseFeedForward, self).__init__()
        self.w_1 = nn.Linear(d_model, d_ff)
        self.w_2 = nn.Linear(d_ff, d_model)
        #self.w_1 = scnn.SeparableConv1d(d_model, d_ff, kernel_size=1)
        #self.w_2 = scnn.SeparableConv1d(d_ff, d_model, kernel_size=1)
        self.dropout = nn.Dropout(dropout)
        self.layer_norm = nn.LayerNorm(d_model, eps=1e-6)

    def forward(self, x):
        residual = x
        output = self.w_2(F.relu(self.w_1(x)))
        output = self.dropout(output)
        output = self.layer_norm(output + residual)
        return output


# Another implementation
class PositionwiseFeedForwardUseConv(nn.Module):
    """A two-feed-forward-layer module"""

    def __init__(self, d_in, d_hid, dropout=0.1):
        super(PositionwiseFeedForwardUseConv, self).__init__()
        self.w_1 = nn.Conv1d(d_in, d_hid, 1, groups=d_in)  # position-wise
        self.w_2 = nn.Conv1d(d_hid, d_in, 1, groups=d_in)  # position-wise
        self.layer_norm = nn.LayerNorm(d_in, eps=1e-06)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        residual = x
        output = x.transpose(1, 2)
        output = self.w_2(F.relu(self.w_1(output)))
        output = output.transpose(1, 2)
        output = self.dropout(output)
        output = self.layer_norm(output + residual)
        return output
