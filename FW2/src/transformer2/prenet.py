import torch.nn as nn

class Pre_Net(nn.Module):
    def __init__(self,d_mel, d_model=512, num_M=2, n=3, c=64,dropout=0.1):
        super(Pre_Net, self).__init__()
        self.d_mel = d_mel
        self.num_M = num_M
        self.d_model = d_model
        self.n = n
        self.c = c

        # Camada convolucional 1D
        self.conv1 = nn.Conv1d(1, c, kernel_size=11, stride=2, padding=2)
        #self.conv1 = nn.Conv1d(1, c, kernel_size=11, stride=2, padding='same')
        #self.bn = nn.BatchNorm2d(c)
        self.relu1 = nn.ReLU()

        # Camada convolucional 1D
        self.conv2 = nn.Conv1d(c, c, kernel_size=11, stride=2, padding=2)
        # self.conv1 = nn.Conv1d(1, c, kernel_size=11, stride=2, padding='same')
        #self.bn2 = nn.BatchNorm2d(c)
        self.relu2 = nn.ReLU()

        # Camada convolucional 1D
        self.conv3 = nn.Conv1d(c, c, kernel_size=11, stride=2, padding=2)
        # self.conv1 = nn.Conv1d(1, c, kernel_size=11, stride=2, padding='same')
        self.relu3 = nn.ReLU()

        # 刚开始直接用列表，没用ModuleList,导致TwoD_Attention_Layer参数权重没有被计入model
        #self.TwoD_layers = nn.ModuleList([TwoD_Attention_Layer(c, c,dropout=dropout) for _ in range(num_M)])

        #self.linear = nn.Linear(d_mel*c//4, d_model)

    def forward(self, inputs):
        '''
        :param inputs: N x Ti x (D_mel*3)
        :return: B*T*d_model
        '''
        B, T, D = inputs.size()
        inputs = inputs.view(B,T,3,-1).permute(0,2,1,3) #N x 3 x Ti x D_mel

        out = self.relu1(self.conv1(inputs))
        print('conv1.shape:', out.shape)
        out = self.relu2(self.conv2(out))
        print('conv2.shape:', out.shape)
        out = self.relu3(self.conv3(out))
        print('conv3.shape:', out.shape)

        B, c, T, D = out.size()

        out = out.permute(0,2,1,3).contiguous().view(B, T, -1) # B*T*(D*c)

        #out = self.linear(out) # B*T*d_model

        return out