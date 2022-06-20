from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import model, schema, utils, Oauth2
from ..database import get_db

router = APIRouter(
    prefix="/votes",
    tags=['Votes']
)

@router.post("/", status_code=status.HTTP_201_CREATED)#, response_model=schema.Votes)
def votes(votes:schema.Votes, db:Session = Depends(get_db), current_user:int=Depends(Oauth2.get_current_user)):
    print(votes)

    query_vote = db.query(model.Post).filter(model.Post.id == votes.post_id).first()
    if query_vote == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {votes.post_id} does not exist")

    vote_query = db.query(model.Votes).filter(model.Votes.post_id==votes.post_id,
                                                model.Votes.user_id==current_user.id)
    found_vote = vote_query.first()
    print(found_vote)
    
    if (votes.dir == 1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"user {current_user.id} has already voted on post {votes.post_id}")
        
        new_vote = model.Votes(post_id=votes.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": f"you voted for post id {votes.post_id}"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="vote does not exist")
        vote_query.delete(synchronize_session=False)
        db.commit()

        return {"message": "successfully deleted your vote"}