import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
import joblib

def analyze_phone_spam(phone_data.csv):
    """
    Simple function to analyze phone spam data
    """
    try:
        # Read the CSV file
        print("Loading data...")
        df = pd.read_csv(backend/phone_data.csv)
        
        # Check if required columns exist
        required_columns = ['phone_number', 'hangup_count', 'spam_reports']
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            print(f"Error: Missing required columns: {missing_columns}")
            print(f"Available columns are: {df.columns.tolist()}")
            return None
            
        # Handle missing values
        df['hangup_count'] = df['hangup_count'].fillna(0)
        df['spam_reports'] = df['spam_reports'].fillna(0)
        
        # Create basic features
        print("Processing features...")
        features = df[['hangup_count', 'spam_reports']]
        
        # Scale features
        scaler = StandardScaler()
        features_scaled = scaler.fit_transform(features)
        
        # Train isolation forest
        print("Training model...")
        iso_forest = IsolationForest(contamination=0.1, random_state=42)
        iso_forest.fit(features_scaled)
        
        # Get anomaly scores
        anomaly_scores = iso_forest.score_samples(features_scaled)
        
        # Calculate final spam score
        df['spam_score'] = -anomaly_scores  # Negative because lower scores indicate anomalies
        
        # Sort and rank
        print("Generating rankings...")
        results = df.sort_values('spam_score', ascending=False)[
            ['phone_number', 'spam_score', 'hangup_count', 'spam_reports']
        ].reset_index(drop=True)
        
        results['rank'] = results.index + 1
        
        print("\nAnalysis complete!")
        return results
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    try:
        # Replace this with your CSV file path
        csv_path = "backend\phone_data.csv"
        
        print(f"Analyzing data from: {csv_path}")
        results = analyze_phone_spam(csv_path)
        
        if results is not None:
            print("\nTop 10 Worst Spam Offenders:")
            print(results.head(10))
            
            # Save results
            output_path = "spam_rankings.csv"
            results.to_csv(output_path, index=False)
            print(f"\nFull results saved to: {output_path}")
            
    except Exception as e:
        print(f"Error in main execution: {str(e)}")
    