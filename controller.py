def scan_image(image_name, body=None):
    """
    Scan an image with the given name and optional parameters
    
    Args:
        image_name: Name of the image (from path parameter)
        body: Optional request body with scan_depth, build_id, build_project
    """
    # Handle empty or None body - set defaults
    if body is None:
        body = {}
    
    # Extract parameters with defaults
    build_id = body.get('build_id')
    build_project = body.get('build_project')
    
    # Perform the actual scan
    result = perform_scan(image_name, build_id, build_project)
    
    # Build response - only include fields that have values
    response = {
        "status": "success",
        "image_name": image_name,
        "result": result
    }
    
    # Add optional fields only if they were provided
    if build_id:
        response["build_id"] = build_id
    if build_project:
        response["build_project"] = build_project
    
    return response, 200


def perform_scan(image_name, build_id=None, build_project=None):
    """
    Actual scanning logic
    
    Args:
        image_name: Name of the image to scan
        scan_depth: Depth of scan (shallow, medium, deep)
        build_id: Optional build ID for tracking
        build_project: Optional project name
    
    Returns:
        Dictionary with scan results
    """
    # Your actual scanning logic here
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
    if build_id or build_project:
        scan_result["build_info"] = {}
        if build_id:
            scan_result["build_info"]["build_id"] = build_id
        if build_project:
            scan_result["build_info"]["build_project"] = build_project
    
    return scan_result