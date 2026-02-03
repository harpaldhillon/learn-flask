from pydantic import BaseModel, Field
from typing import Optional


class BuildContext(BaseModel):
    """Build context information for tracking scans"""
    build_id: str = Field(..., description="Unique build identifier")
    build_name: str = Field(..., description="Name of the build")
    build_repo: str = Field(..., description="Repository URL or name")
    
    class Config:
        schema_extra = {
            "example": {
                "build_id": "build-12345",
                "build_name": "prod-release-v1.2.3",
                "build_repo": "github.com/myorg/myrepo"
            }
        }


class ScanRequest(BaseModel):
    build_context: Optional[BuildContext] = Field(
        default=None,
        description="Optional build context for tracking"
    )
    
    class Config:
        schema_extra = {
            "example": {
                "build_context": {
                    "build_id": "build-12345",
                    "build_name": "prod-release-v1.2.3",
                    "build_repo": "github.com/myorg/myrepo"
                }
            }
        }