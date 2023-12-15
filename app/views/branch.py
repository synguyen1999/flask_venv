from flask import Flask, request, jsonify
from app.views import branch_blueprint

from app import db, client, loaded_model


@branch_blueprint.route("/getBranch", methods=["GET"])
def get_branch():
    try:
        # Access the 'test' collection in the MongoDB database
        collection = db["items"]

        # Example query: find documents where 'some_key' is 'some_value'
        cursor = collection.find()

        # Retrieve data from the cursor
        data = [doc for doc in cursor]

        if data:
            # Format the retrieved data for display (you might adjust this based on your data structure)
            return jsonify(data)
        else:
            return "No data found in 'test' collection"
    except Exception as e:
        return f"Error querying 'test' collection: {e}"


# router.get("/getBranch", async (req, res) => {
#   try {
#     let branches = await Branch.find();

#     const data = {
#       success: true,
#       message: "All Branches Loaded!",
#       branches,
#     };
#     res.json(data);
#   } catch (error) {
#     console.error(error.message);
#     res.status(500).json({ success: false, message: "Internal Server Error" });
#   }
# });
