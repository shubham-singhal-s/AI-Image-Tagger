import fiftyone as fo
import fiftyone.zoo as foz

#
# Load 50 random samples from the validation split
#
# Only the required images will be downloaded (if necessary).
# By default, all label types are loaded

data = ["Cat", "Dog", "Bird"]

dataset = foz.load_zoo_dataset(
    "open-images-v6",
    split="train",
    label_types=["classifications"],
    classes=data,
    max_samples=10000,
)

dataset = foz.load_zoo_dataset(
    "open-images-v6",
    split="validation",
    label_types=["classifications"],
    classes=data,
    max_samples=2000,
)

dataset = foz.load_zoo_dataset(
    "open-images-v6",
    split="test",
    label_types=["classifications"],
    classes=data,
    max_samples=2000,
)
