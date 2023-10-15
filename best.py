import hydra
from omegaconf import DictConfig, OmegaConf


@hydra.main(config_path="configs/test6", config_name="config", version_base="1.3")
def hydra_run(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))


if __name__ == '__main__':
    hydra_run()
