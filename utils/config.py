from dotenv import load_dotenv
import os
from enum import Enum

load_dotenv()

SCENARIO_PLANNER_PAGE = os.getenv("SCENARIO_PLANNER_PAGE")
META_URL = os.getenv('META_URL')


class EnvironmentConfig(Enum):
    USA_UAT = "usa_uat"
    USA_STAGE = "usa_stage"
    CHINA_PROD = "china_prod"
    AUSTRALIA_PROD = "australia_prod"


ENVIRONMENTS = {
    EnvironmentConfig.USA_UAT: {
        "base_url": os.getenv('USA_UAT_BASE_URL'),
        "username": os.getenv('USA_UAT_USERNAME'),
        "password": os.getenv('USA_UAT_PASSWORD')
    },
    EnvironmentConfig.USA_STAGE: {
        "base_url": os.getenv('USA_STAGE_BASE_URL'),
        "username": os.getenv('USA_STAGE_USERNAME'),
        "password": os.getenv('USA_STAGE_PASSWORD')
    },
    EnvironmentConfig.CHINA_PROD: {
        "base_url": os.getenv('CHINA_PROD_BASE_URL'),
        "username": os.getenv('CHINA_PROD_USERNAME'),
        "password": os.getenv('CHINA_PROD_PASSWORD')
    },
    EnvironmentConfig.AUSTRALIA_PROD: {
        "base_url": os.getenv('AUSTRALIA_PROD_BASE_URL'),
        "username": os.getenv('AUSTRALIA_PROD_USERNAME'),
        "password": os.getenv('AUSTRALIA_PROD_PASSWORD')
    }
}
