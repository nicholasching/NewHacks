import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.ensemble import RandomForestClassifier
import joblib
from datetime import datetime

class SpamCallAnalyzer:
    def __init__(self):
        self.scaler = StandardScaler()
        self.isolation_forest = IsolationForest(contamination=0.1, random_state=42)
        self.random_forest = RandomForestClassifier(n_estimators=100, random_state=42)
        
    def load_data(self, csv_path):
        """
        Load and preprocess the CSV data
        """
        # Read the CSV file
        df = pd.read_csv(csv_path)
        
        # Handle missing values
        df = df.fillna({
            'hangup_count': 0,
            'hangup_time': df['hangup_time'].mean(),
            'spam_reports': 0,
            'call_duration': df['call_duration'].mean(),
            'time_of_day': '12:00'  # Default to noon for missing times
        })
        
        return df
    
    def extract_features(self, df):
        """
        Extract and engineer features from the raw data
        """
        # Convert time_of_day to hour (assuming format HH:MM)
        df['hour'] = pd.to_datetime(df['time_of_day'], format='%H:%M').dt.hour
        
        # Calculate time-based risk factors
        df['night_caller'] = ((df['hour'] < 6) | (df['hour'] > 21)).astype(int)
        
        # Calculate rate-based features
        df['hangup_rate'] = df['hangup_count'] / df['total_calls']
        df['short_call_rate'] = (df['call_duration'] < 10).sum() / df['total_calls']
        
        # Create feature matrix
        feature_columns = [
            'hangup_count',
            'hangup_time',
            'spam_reports',
            'call_duration',
            'hangup_rate',
            'short_call_rate',
            'night_caller'
        ]
        
        X = df[feature_columns]
        return X, feature_columns
    
    def train_models(self, X):
        """
        Train the anomaly detection and classification models
        """
        # Scale the features
        X_scaled = self.scaler.fit_transform(X)
        
        # Train Isolation Forest for anomaly detection
        self.isolation_forest.fit(X_scaled)
        
        # Generate synthetic labels based on anomaly detection
        synthetic_labels = (self.isolation_forest.predict(X_scaled) == -1).astype(int)
        
        # Train Random Forest classifier
        self.random_forest.fit(X_scaled, synthetic_labels)
        
        return X_scaled
    
    def calculate_spam_score(self, X_scaled, X_original):
        """
        Calculate a comprehensive spam score using multiple factors
        """
        # Get anomaly scores (-1 for anomalies, 1 for normal)
        anomaly_scores = self.isolation_forest.score_samples(X_scaled)
        
        # Get probability scores from Random Forest
        spam_probabilities = self.random_forest.predict_proba(X_scaled)[:, 1]
        
        # Create a weighted combination of factors
        weights = {
            'anomaly_score': 0.3,
            'spam_probability': 0.3,
            'spam_reports': 0.2,
            'hangup_rate': 0.2
        }
        
        # Normalize anomaly scores to 0-1 range
        normalized_anomaly_scores = (anomaly_scores - anomaly_scores.min()) / (anomaly_scores.max() - anomaly_scores.min())
        
        # Calculate final spam score
        spam_score = (
            weights['anomaly_score'] * normalized_anomaly_scores +
            weights['spam_probability'] * spam_probabilities +
            weights['spam_reports'] * (X_original['spam_reports'] / X_original['spam_reports'].max()) +
            weights['hangup_rate'] * X_original['hangup_rate']
        )
        
        return spam_score
    
    def analyze_phone_numbers(self, csv_path, output_path=None):
        """
        Main function to analyze phone numbers and generate rankings
        """
        # Load and preprocess data
        df = self.load_data(csv_path)
        
        # Extract features
        X, feature_columns = self.extract_features(df)
        
        # Train models
        X_scaled = self.train_models(X)
        
        # Calculate spam scores
        spam_scores = self.calculate_spam_score(X_scaled, X)
        
        # Add scores to dataframe
        df['spam_score'] = spam_scores
        
        # Sort by spam score and create rankings
        results = df.sort_values('spam_score', ascending=False)[
            ['phone_number', 'spam_score', 'hangup_count', 'spam_reports', 'hangup_rate']
        ].reset_index(drop=True)
        
        # Add rank column
        results['rank'] = results.index + 1
        
        # Save results if output path is provided
        if output_path:
            results.to_csv(output_path, index=False)
            print(f"Results saved to {output_path}")
        
        return results
    
    def save_model(self, path):
        """
        Save the trained model for future use
        """
        model_data = {
            'scaler': self.scaler,
            'isolation_forest': self.isolation_forest,
            'random_forest': self.random_forest
        }
        joblib.dump(model_data, path)
        
    def load_model(self, path):
        """
        Load a previously trained model
        """
        model_data = joblib.load(path)
        self.scaler = model_data['scaler']
        self.isolation_forest = model_data['isolation_forest']
        self.random_forest = model_data['random_forest']

# Example usage
if __name__ == "__main__":
    # Initialize the analyzer
    analyzer = SpamCallAnalyzer()
    
    # Analyze phone numbers
    results = analyzer.analyze_phone_numbers(
        csv_path="phone_data.csv",
        output_path="spam_rankings.csv"
    )
    
    # Print top 10 worst offenders
    print("\nTop 10 Worst Spam Offenders:")
    print(results.head(10))
    
    # Save the trained model
    analyzer.save_model("spam_analyzer_model.joblib")