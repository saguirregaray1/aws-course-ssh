import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import {
  DynamoDBDocumentClient,
  ScanCommand,
  PutCommand,
  GetCommand,
  DeleteCommand,
} from "@aws-sdk/lib-dynamodb";

const client = new DynamoDBClient({});

const dynamo = DynamoDBDocumentClient.from(client);

const tableName = "apps_queries";
const tableName1 = "ratings_queries"

export const handler = async (event, context) => {
  let body;
  let statusCode = 200;
  const headers = {
    "Content-Type": "application/json",
  };

  try {
    switch (event.routeKey) {
      case "GET /apps/installs/{category}":
        body = await dynamo.send(
          new GetCommand({
            TableName: tableName,
            Key: {
              category: event.pathParameters.category,
            },
          })
        );
        body = body.Item;
        break;
      case "GET /apps/installs":
        body = await dynamo.send(
          new ScanCommand({ TableName: tableName })
        );
        body = body.Items;
        break;
      case "GET /apps/ratings/{category}":
        body = await dynamo.send(
          new GetCommand({
            TableName: tableName1,
            Key: {
              category: event.pathParameters.category,
            },
          })
        );
        body = body.Item;
        break;
      case "GET /apps/ratings":
        body = await dynamo.send(
          new ScanCommand({ TableName: tableName1 })
        );
        body = body.Items;
        break;
      default:
        throw new Error(`Unsupported route: "${event.routeKey}"`);
    }
  } catch (err) {
    statusCode = 400;
    body = err.message;
  } finally {
    body = JSON.stringify(body);
  }

  return {
    statusCode,
    body,
    headers,
  };
};

