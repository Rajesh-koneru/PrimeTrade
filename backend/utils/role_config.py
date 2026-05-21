from utils.authenticate import is_authenticate
from schemas.Verify_JWT import get_current_user
from fastapi import HTTPException,Depends

def require_role(allowed_roles: list):

    def role_checker(
        current_user = Depends(get_current_user)
    ):

        if current_user["role"] not in allowed_roles:
            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

        return current_user

    return role_checker