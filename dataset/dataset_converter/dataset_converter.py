import json
import datasets

_DESCRIPTION = """\
A high-quality dataset for efficient instruction tuning.
"""

class LimaConfig(datasets.BuilderConfig):
    """BuilderConfig"""

    def __init__(self, **kwargs):
        """BuilderConfig
        Args:
          **kwargs: keyword arguments forwarded to super.
        """
        super(LimaConfig, self).__init__(**kwargs)


class Lima(datasets.GeneratorBasedBuilder):

    BUILDER_CONFIGS = [
        LimaConfig(
            name="plain_text",
            version=datasets.Version("0.0.1", ""),
            description="Plain text",
        ),
    ]

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "conversations": datasets.features.Sequence(datasets.Value("string")),
                    "source": datasets.Value("string"),
                }
            ),
        )

    def _split_generators(self, dl_manager):
        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"filepath": dl_manager.download("full_data.jsonl")}),
            #datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={"filepath":dl_manager.download("test.jsonl")})
        ]

    def _generate_examples(self, filepath):
        """This function returns the examples in the raw (text) form."""
        key = 0
        with open(filepath) as f:
            for line in f.readlines():
                instance = json.loads(line)
                yield key, instance
                key += 1