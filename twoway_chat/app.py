import autogen

def main():
    config_list=autogen.config_list_from_json(
        env_or_file="OAI_CONFIG_LIST.json"
    )