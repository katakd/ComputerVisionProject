# Semi-supervised Image Classification Project

## Methods
We implement these following methods:
- Pseudo label [1](https://www.researchgate.net/publication/280581078_Pseudo-Label_The_Simple_and_Efficient_Semi-Supervised_Learning_Method_for_Deep_Neural_Networks)
- Pi model [2](https://arxiv.org/abs/1610.02242)
- FixMatch [3](https://arxiv.org/abs/2001.07685)
- Noisy student [4](https://arxiv.org/abs/1911.04252) 


## Code
* For training these methods with our defined configuration, run the following command:
```
python3 main.py --method <method_name>
```

with `method_name` is one of [`fixmatch`, `noisy`, `pi`,`pseudo`]

