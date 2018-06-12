from app import app, db, models

@app.shell_context_processor
def _():
	return {'db': db, 'Post': models.Post, 'Comment':models.Comment}
