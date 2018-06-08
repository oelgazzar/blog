from app import app

@app.shell_context_processor
def _():
	return {'db': db, 'Post': Post, 'Category': Category}
