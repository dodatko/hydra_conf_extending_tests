# import hydra
from omegaconf import DictConfig, OmegaConf
import os

# @hydra.main(config_path="configs/test6", config_name="config", version_base="1.3")
# def hydra_run(cfg : DictConfig) -> None:
#     print(OmegaConf.to_yaml(cfg))


if __name__ == '__main__':
    OmegaConf.register_new_resolver("os_cpu_count", lambda: os.cpu_count())
    my_yaml = """
    trainer:
        cpu_count: ${os_cpu_count:}
    """
    cfg = OmegaConf.create(my_yaml)
    # print(OmegaConf.to_yaml(cfg))
    print(cfg.trainer.cpu_count)

    # hydra_run()
