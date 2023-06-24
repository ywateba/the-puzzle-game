resource "aws_lambda_function" "example_lambda" {
  function_name = "example_lambda_function"
  handler = "lambda_function.lambda_handler"
  runtime = "python3.8"
  filename = "example_lambda.zip"
  source_code_hash = filebase64sha256("example_lambda.zip")
  role = aws_iam_role.lambda_execution.arn
}

resource "aws_iam_role" "lambda_execution" {
  name = "lambda_execution_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })

  tags = {
    Terraform   = "true"
    Environment = "dev"
  }
}

resource "aws_dynamodb_table" "example_table" {
  name           = "example_table"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "id"
  attribute {
    name = "id"
    type = "S"
  }
  attribute {
    name = "name"
    type = "S"
  }
  attribute {
    name = "age"
    type = "N"
  }
}
