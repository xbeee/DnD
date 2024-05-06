import React, { useState } from "react";
import User from "./pages/User";
import Login from "./pages/Login";
import AppContext from "./context";
import { Routes, Route, BrowserRouter, Navigate } from "react-router-dom";
import useToken from "./hooks/useToken";

const App = () => {
	const { setToken, getToken } = useToken();
	const [mainToken, setMainToken] = React.useState(null);
	React.useEffect(() => {
		const token = getToken();
		setToken(token);
		setMainToken(token);
	}, []);

	return (
		<AppContext.Provider value={{ mainToken }}>
			<BrowserRouter>
				<Routes>
					<Route
						path="/"
						element={mainToken ? <User /> : <Navigate to="/login" />}
					/>
					<Route
						path="/login"
						element={mainToken ? <Navigate to="/" /> : <Login />}
					/>
				</Routes>
			</BrowserRouter>
		</AppContext.Provider>
	);
};

export default App;
