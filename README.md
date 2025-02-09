<div align="left" style="position: relative;">
<img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" align="right" width="30%" style="margin: -20px 0 0 20px;">
<h1>LLM-COMPARE-FASTAPI</h1>
<p align="left">
	<em>Unleashing AI Power, One Language Model at a Time!</em>
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/serkanyasr/LLM-Compare-FastAPI?style=default&logo=opensourceinitiative&logoColor=white&color=079e8c" alt="license">
	<img src="https://img.shields.io/github/last-commit/serkanyasr/LLM-Compare-FastAPI?style=default&logo=git&logoColor=white&color=079e8c" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/serkanyasr/LLM-Compare-FastAPI?style=default&color=079e8c" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/serkanyasr/LLM-Compare-FastAPI?style=default&color=079e8c" alt="repo-language-count">
</p>
<p align="left"><!-- default option, no dependency badges. -->
</p>
<p align="left">
	<!-- default option, no dependency badges. -->
</p>
</div>
<br clear="right">

![Ekran görüntüsü 2025-02-09 111241](https://github.com/user-attachments/assets/9916a1d7-0018-4145-8601-d83f5da24747)


## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

LLM-Compare-FastAPI is an innovative open-source project designed to streamline the comparison of various AI language models. It leverages FastAPI and Streamlit to create a user-friendly interface where users can input prompts and view responses from different models, including DeepSeek, OpenAI GPT, Google Gemini, Anthropic Claude, and Cohere Command. The project offers a unique solution for AI enthusiasts, researchers, and developers seeking to evaluate and understand the nuances of different language models in a simple, efficient manner.

---

## 👾 Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>The project uses a two-tier application architecture, with a backend service built with `FastAPI` and a frontend service using `Streamlit`.</li><li>The backend and frontend services are orchestrated using a `docker-compose.yml` file, ensuring both services run on a shared network.</li><li>The backend service is responsible for language processing tasks and server operations, while the frontend service handles user interaction and API calls to the backend.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>The project is written primarily in `Python`, with a clean and modular code structure.</li><li>It uses `Docker` for containerization, enhancing the project's portability and scalability.</li><li>The project leverages the `dotenv` module to securely load and store keys for various AI services.</li></ul> |
| 📄 | **Documentation** | <ul><li>The project provides detailed installation and usage commands for both `pip` and `docker`.</li><li>It outlines the necessary dependencies for both the backend and frontend services in `requirements.txt` files.</li><li>The project also provides a test command using `pytest`.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>The project integrates with various AI services such as `DeepSeek`, `OpenAI`, `Google AI`, `Anthropic`, and `Cohere`.</li><li>It provides routes to generate text using different AI models via the `endpoints.py` file in the backend application.</li><li>The frontend service makes API calls to the backend and displays response times.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>The project is structured into separate backend and frontend services, each with its own `Dockerfile` and `requirements.txt` file.</li><li>The backend service is further divided into core and API modules, with a central `config.py` file for managing API keys.</li><li>The frontend service is encapsulated in a single `app.py` file, handling user interaction and API calls.</li></ul> |
| 🧪 | **Testing**       | <ul><li>The project provides a test command using `pytest`.</li><li>However, specific test cases or test files are not mentioned in the provided context details.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>The project uses `FastAPI` for the backend service, known for its high performance and asynchronous capabilities.</li><li>The frontend service uses `Streamlit`, enabling rapid prototyping and efficient user interaction.</li></ul> |
| 🛡️ | **Security**      | <ul><li>The project uses the `dotenv` module to securely load and store keys for various AI services.</li><li>However, specific security measures or practices are not mentioned in the provided context details.</li></ul> |

---

## 📁 Project Structure

```sh
└── LLM-Compare-FastAPI/
    ├── LICENSE
    ├── README.md
    ├── backend
    │   ├── Dockerfile
    │   ├── app
    │   └── requirements.txt
    ├── docker-compose.yml
    └── frontend
        ├── Dockerfile
        ├── app.py
        └── requirements.txt
```


### 📂 Project Index
<details open>
	<summary><b><code>LLM-COMPARE-FASTAPI/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/serkanyasr/LLM-Compare-FastAPI/blob/master/docker-compose.yml'>docker-compose.yml</a></b></td>
				<td>- The docker-compose.yml orchestrates the deployment of a two-tier application architecture, comprising a backend service built with FastAPI and a frontend service using Streamlit<br>- It ensures both services run on a shared network, with the frontend service dependent on the backend, and both services restarting automatically if they fail.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- backend Submodule -->
		<summary><b>backend</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/serkanyasr/LLM-Compare-FastAPI/blob/master/backend/requirements.txt'>requirements.txt</a></b></td>
				<td>- Backend/requirements.txt outlines the necessary dependencies for the project, including various language processing libraries and server frameworks<br>- It ensures the correct packages are installed for the backend to function properly, facilitating language processing tasks and server operations.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/serkanyasr/LLM-Compare-FastAPI/blob/master/backend/Dockerfile'>Dockerfile</a></b></td>
				<td>- The Dockerfile in the backend directory sets up a Python-based environment, installs necessary dependencies from the requirements.txt file, and prepares the application for running on a server<br>- It enables the application to be containerized and run consistently across different platforms, enhancing the project's portability and scalability.</td>
			</tr>
			</table>
			<details>
				<summary><b>app</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/serkanyasr/LLM-Compare-FastAPI/blob/master/backend/app/main.py'>main.py</a></b></td>
						<td>- Main.py, located in the backend/app directory, serves as the entry point for the FastAPI LangChain API<br>- It integrates the application's endpoints and initiates the FastAPI server<br>- The code's execution starts the server locally on port 8000, enabling the API's functionality.</td>
					</tr>
					</table>
					<details>
						<summary><b>core</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/serkanyasr/LLM-Compare-FastAPI/blob/master/backend/app/core/config.py'>config.py</a></b></td>
								<td>- Config.py serves as a central hub for managing API keys within the backend of the application<br>- It leverages the dotenv module to securely load and store keys for various AI services such as OpenAI, Google AI, Anthropic, and Cohere<br>- This configuration ensures seamless integration and secure communication with these external services.</td>
							</tr>
							<tr>
								<td><b><a href='https://github.com/serkanyasr/LLM-Compare-FastAPI/blob/master/backend/app/core/models.py'>models.py</a></b></td>
								<td>- The core/models.py module in the backend application serves as an interface for various AI chat models<br>- It provides functions to interact with GPT-3.5 Turbo, Gemini, Claude-2.1, and ChatCohere models, enabling the sending of prompts and receiving of AI-generated responses<br>- This module plays a crucial role in facilitating AI-based conversations in the project.</td>
							</tr>
							</table>
						</blockquote>
					</details>
					<details>
						<summary><b>api</b></summary>
						<blockquote>
							<table>
							<tr>
								<td><b><a href='https://github.com/serkanyasr/LLM-Compare-FastAPI/blob/master/backend/app/api/endpoints.py'>endpoints.py</a></b></td>
								<td>- The 'endpoints.py' in the backend application serves as the API gateway, providing routes to generate text using different AI models - OpenAI GPT, Google Gemini, Anthropic Claude, and Cohere Command<br>- It also includes a route to check the API's health status.</td>
							</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- frontend Submodule -->
		<summary><b>frontend</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/serkanyasr/LLM-Compare-FastAPI/blob/master/frontend/app.py'>app.py</a></b></td>
				<td>- The frontend/app.py serves as the user interface for the LangChain project, facilitating user interaction with multiple language models<br>- It allows users to input a prompt, adjust model settings, and view responses from different models, including OpenAI GPT, Google Gemini, Anthropic Claude, and Cohere Command<br>- The file also handles API calls to the backend and displays response times.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/serkanyasr/LLM-Compare-FastAPI/blob/master/frontend/requirements.txt'>requirements.txt</a></b></td>
				<td>- Frontend/requirements.txt outlines the necessary Python packages for the frontend component of the project<br>- It specifies 'streamlit' and 'requests' as dependencies, ensuring the application's user interface runs smoothly and can make HTTP requests<br>- This file plays a crucial role in maintaining the project's environment consistency.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/serkanyasr/LLM-Compare-FastAPI/blob/master/frontend/Dockerfile'>Dockerfile</a></b></td>
				<td>- The Dockerfile in the frontend directory sets up a Python environment, installs necessary dependencies from the requirements.txt file, and prepares the application for execution<br>- It specifically configures Streamlit to run the app.py file, making the application accessible via a specified server port and address.</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with LLM-Compare-FastAPI, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip
- **Container Runtime:** Docker


### ⚙️ Installation

Install LLM-Compare-FastAPI using one of the following methods:

**Build from source:**

1. Clone the LLM-Compare-FastAPI repository:
```sh
❯ git clone https://github.com/serkanyasr/LLM-Compare-FastAPI
```

2. Navigate to the project directory:
```sh
❯ cd LLM-Compare-FastAPI
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r backend/requirements.txt, frontend/requirements.txt
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker build -t serkanyasr/LLM-Compare-FastAPI .
```




### 🤖 Usage
Run LLM-Compare-FastAPI using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker run -it {image_name}
```


### 🧪 Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```


## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/serkanyasr/LLM-Compare-FastAPI/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/serkanyasr/LLM-Compare-FastAPI/issues)**: Submit bugs found or log feature requests for the `LLM-Compare-FastAPI` project.
- **💡 [Submit Pull Requests](https://github.com/serkanyasr/LLM-Compare-FastAPI/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/serkanyasr/LLM-Compare-FastAPI
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/serkanyasr/LLM-Compare-FastAPI/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=serkanyasr/LLM-Compare-FastAPI">
   </a>
</p>
</details>

---

## 🎗 License

This project is licensed under the MIT License.For more details, refer to the [LICENSE](https://github.com/serkanyasr/LLM-Compare-FastAPI/blob/main/LICENSE) file.

---

