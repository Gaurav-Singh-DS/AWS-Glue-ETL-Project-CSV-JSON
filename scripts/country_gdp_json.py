import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node Amazon S3
AmazonS3_node1757098800463 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://projectglueaw2025/Source/"], "recurse": True}, transformation_ctx="AmazonS3_node1757098800463")

# Script generated for node Change Schema
ChangeSchema_node1757098934134 = ApplyMapping.apply(frame=AmazonS3_node1757098800463, mappings=[("country", "string", "country", "string"), ("gdp", "string", "Gross_domestic_price", "string")], transformation_ctx="ChangeSchema_node1757098934134")

# Script generated for node Target
EvaluateDataQuality().process_rows(frame=ChangeSchema_node1757098934134, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1757098787982", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
Target_node1757099146954 = glueContext.write_dynamic_frame.from_options(frame=ChangeSchema_node1757098934134, connection_type="s3", format="json", connection_options={"path": "s3://projectglueaw2025/Target/", "partitionKeys": []}, transformation_ctx="Target_node1757099146954")

job.commit()