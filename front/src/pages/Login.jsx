import React, { useState } from "react";
import axios from "axios";
import useToken from "../hooks/useToken";
import { Navigate } from "react-router-dom";

const LoginForm = () => {
	const [name, setName] = React.useState("");
	const [error, setError] = React.useState(null);
	const { setToken, getToken } = useToken();
	const token = getToken();

	const handleSubmit = async (event) => {
		event.preventDefault();
		try {
			const formData = new FormData();
			formData.append("name", name);
			const response = await axios.post("http://localhost:5000/login", formData);

			setToken(response.data.access_token);

			localStorage.setItem("name", name);

			window.location.href = "/";
		} catch (error) {
			if (error.response) {
				setError(error.response.data.errString);
				console.error("Ошибка ответа от сервера:", error.response.data);
			} else {
				setError("Произошла ошибка при выполнении запроса");
				console.error("Ошибка запроса:", error.message);
			}
		}
	};

	const handleChange = (event) => {
		setName(event.target.value);
	};

	return (
		<div>
			<h2>Форма входа</h2>
			{error && <div style={{ color: "red" }}>{error}</div>}
			<form
				onSubmit={handleSubmit}
				method="POST"
			>
				<div>
					<label htmlFor="name">Имя:</label>
					<input
						type="text"
						id="name"
						name="name"
						value={name}
						onChange={handleChange}
					/>
				</div>
				<button type="submit">Войти</button>
			</form>
		</div>
	);
};

export default LoginForm;
