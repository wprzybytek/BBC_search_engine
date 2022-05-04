const ArticlesList = ({ articles }) => {
  return (
    <div className="row justify-content-center offset-sm-2 col-sm-8">
      {articles.map((article) => (
        <div className="card">
          <div className="card-body">
            <h5 className="card-title">{article.title}</h5>
            <p className="card-text">{article.content}</p>
            <p className="card-text">
              <small className="text-muted">{article.category}</small>
            </p>
          </div>
        </div>
      ))}
    </div>
  );
};

export default ArticlesList;
