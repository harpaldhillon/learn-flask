from typing import Optional
from models import BuildContext, ScanRequest
from pydantic import ValidationError


def scan_image(image_name: str, body: Optional[dict] = None):
    """
    Scan an image with optional parameters
    
    Args:
        image_name: Name of the image (from path parameter)
        body: Optional request body with scan parameters and build context
    """
    # Handle empty or None body
    if body is None or body == {}:
        body = {}
    
    try:
        # Parse and validate request body using Pydantic
        scan_request = ScanRequest(**body)
        
        # Extract validated data
        build_context = scan_request.build_context
        
    except ValidationError as e:
        # Return validation errors
        return {
            "status": "error",
            "message": "Validation failed",
            "errors": [
                {
                    "field": ".".join(str(loc) for loc in err["loc"]),
                    "message": err["msg"],
                    "type": err["type"]
                }
                for err in e.errors()
            ]
        }, 400
    
    # Perform the actual scan
    result = perform_scan(image_name, build_context)
    
    # Build response
    response = {
        "status": "success",
        "image_name": image_name,
        "result": result
    }
    
    # Include build_context in response if it was provided
    if build_context:
        response["build_context"] = build_context.model_dump()
    
    return response, 200


def perform_scan(
    image_name: str,
    build_context: Optional[BuildContext] = None
):
    """
    Actual scanning logic
    
    Args:
        image_name: Name of the image to scan
        scan_depth: Depth of scan (shallow, medium, deep)
        build_context: Optional build context information
    
    Returns:
        Dictionary with scan results
    """
    scan_result = {
        "scanned_at": "2026-02-03T10:30:00Z",
        "findings": [
            {"type": "vulnerability", "severity": "medium", "count": 3},
            {"type": "misconfiguration", "severity": "low", "count": 1}
        ],
        "scan_duration_seconds": 12.5,
        "total_layers": 15,
        "scanned_layers": 15
    }
    
    # Add build tracking info if provided
    if build_context:
        scan_result["build_info"] = {
            "build_id": build_context.build_id,
            "build_name": build_context.build_name,
            "build_repo": build_context.build_repo,
            "tracked_at": "2026-02-03T10:30:00Z"
        }
    
    return scan_result