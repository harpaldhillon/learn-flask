import connexion
import os

app = connexion.App(__name__, specification_dir='./')
app.add_api('openapi.yaml')

if __name__ == '__main__':
    # Enable remote debugging when in Docker
    if os.environ.get('ENABLE_DEBUGPY') == '1':
        import debugpy
        debugpy.listen(("0.0.0.0", 5678))
        print("⏳ Waiting for debugger to attach...")
        debugpy.wait_for_client()
        print("✅ Debugger attached!")
    
    app.run(host='0.0.0.0', port=5000)