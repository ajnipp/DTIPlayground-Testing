from dmri.common.tools.base import ExternalToolWrapper

class GreedyAtlas(ExternalToolWrapper):
    def __init__(self,binary_path):
        super().__init__(binary_path)

    def compute_deformation_fields(self,xml_file,parsed_file):
        arguments=[
            '-f',xml_file,
            '-o',parsed_file
        ]
        self.setArguments(arguments)
        return self.execute(arguments)