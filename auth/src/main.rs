use axum::{Json, Router, routing::get};
mod entities;
use serde::{Deserialize, Serialize};

#[derive(Deserialize)]
struct CreateUser {
    username: String,
}

#[derive(Serialize)]
struct UserResponse {
    id: i32,
    username: String,
}
#[tokio::main]
async fn main() {
    // Build router
    let app = Router::new()
        .route("/", get(root_handler))
        .route("/hello", get(hello_handler));

    // Start server
    let addr = SocketAddr::from(([127, 0, 0, 1], 3000));
    println!("Listening on http://{}", addr);
    let listener = tokio::net::TcpListener::bind(&addr).await.unwrap();
    axum::serve(listener, app.into_make_service())
        .await
        .unwrap();
}

async fn root_handler() -> &'static str {
    "Welcome to your Axum API!"
}

async fn hello_handler() -> Json<HelloResponse> {
    let response = HelloResponse {
        message: "Hello from Axum!".to_string(),
    };
    Json(response)
}
