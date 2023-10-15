## How to extend package using parameters from any other package

### Motivation
.... 


### Sweep
`python main.py +trainer/gpu@trainer=2x2080,rtx2070,gpu_rtx2070 -m`


### Files tree:
```
├── configs
    ├── trainer
    │   ├── gpu
    │   │   ├── 2x3090.yaml
    │   │   └── a6000.yaml
    │   └─── defaults.yaml
    └── config.yaml
```


### 3 ways to do 

#### 1. [Overriding the package via the package directive](https://hydra.cc/docs/advanced/overriding_packages/#overriding-the-package-via-the-package-directive)
`# @package trainer` in the head of file to change default package
[example](configs/test5/trainer/gpu/2x2080.yaml): `configs/test5/trainer/gpu/2x2080.yaml`


#### 2.  [Extending a config from another config group](https://hydra.cc/docs/patterns/extending_configs/)
[example](configs/test5/trainer/defaults.yaml):
```
defaults:
  - base
  - gpu/gpu_rtx2070@_here_
```
in `configs/test5/trainer/defaults.yaml`


#### 3. [Overriding packages using the Defaults List](https://hydra.cc/docs/advanced/overriding_packages/#overriding-packages-using-the-defaults-list)
**Best way?**

[example](configs/test6/config.yaml) `configs/test6/config.yaml`
```
defaults:
  - _self_
  - trainer: defaults
#  - gpu/rtx2070@trainer
  - gpu@trainer: rtx2070
```

Files tree:
```
├── configs
    ├── gpu
    │   ├── 2x3090.yaml
    │   └── a6000.yaml
    ├── trainer
    │   └─── defaults.yaml
    └── config.yaml
```

... and without `# @package trainer` redundant headers

### Custom variables like os.cpu_count
Implemented using OmegaConf resolvers, [see example here](resolvers.py)


### TODO
1. [ ] Motivation section
1. [ ] Resolvers example
1. [ ] Rename configs/* with descriptive names
