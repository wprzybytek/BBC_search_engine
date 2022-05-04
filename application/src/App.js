import { useState } from "react";
import getArticles from "./apis/request.js";
import ArticlesList from "./components/ArticlesList.js";

function App() {
  const [text, setText] = useState("");
  const [articles, setArticles] = useState([]);

  const onSubmit = async (e) => {
    e.preventDefault();
    if (text) {
      const data = await getArticles(text);
      setArticles(data);
    }
  };

  return (
    <div className="container-fluid ">
      <form
        className="input-group d-flex justify-content-center m-4"
        onSubmit={onSubmit}
      >
        <div className="form-outline w-50">
          <input
            type="search"
            id="form1"
            className="form-control"
            values={text}
            onChange={(e) => setText(e.target.value)}
          />
        </div>
        <button type="submit" className="btn btn-primary">
          Search
        </button>
      </form>
      <ArticlesList articles={articles} />
    </div>
  );
}

export default App;
